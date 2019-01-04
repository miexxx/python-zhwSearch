# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from search.models import ArticleType,ZhihuAnswerType,ZhihuQuestionType,LagouType
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
import json
from elasticsearch import Elasticsearch
from datetime import datetime
import redis
# Create your views here.
client = Elasticsearch(hosts=["127.0.0.1"])
redis_cli = redis.StrictRedis()

class IndexView(View):
    def get(self, request):
        topn_search = redis_cli.zrevrangebyscore("search_keywords_set", "+inf", "-inf", start=0, num=5)
        return render(request, "index.html", {"topn_search":topn_search})
class SearchSuggest(View):
    def get(self, request):
        key_words = request.GET.get('s', '')
        date_type = request.GET.get('s_type', 'article')
        re_datas = []
        if key_words:
            if date_type == "article":
                s = ArticleType.search()
            if date_type == "question":
                s = ZhihuQuestionType.search()
            if date_type == "job":
                s = LagouType.search()
            s = s.suggest('my_suggest', key_words, completion={
                "field":"suggest", "fuzzy":{
                    "fuzziness":2
                },
                "size": 10
            })
            suggestions = s.execute()
            for match in suggestions.suggest.my_suggest[0].options:
                source = match._source
                title="".join(source["title"])
                re_datas.append(title)
        return HttpResponse(json.dumps(re_datas), content_type="application/json")

class SearchView(View):
    def get(self, request):
        key_words = request.GET.get("q","")
        redis_cli.zincrby("search_keywords_set", key_words)
        date_type = request.GET.get('s_type', 'article')

        topn_search = redis_cli.zrevrangebyscore("search_keywords_set", "+inf", "-inf", start=0, num=5)
        page = request.GET.get("p","0")
        try:
            page = int(page)
        except:
            page = 0
        jobbole_count = redis_cli.get("jobbole_count")
        zhihu_count = redis_cli.incr("zhihu_count")
        lagou_count = redis_cli.incr("lagou_count")
        star_time = datetime.now()
        response =self.get_response(date_type, key_words, page)
        end_time = datetime.now()
        last_secondes = (end_time - star_time).total_seconds()
        total_nums = response["hits"]["total"]
        if (page%10) > 0:
            page_nums = int(total_nums/10) +1
        else:
            page_nums = int(total_nums/10)
        hit_list = []
        if date_type == "job":
            for hit in response["hits"]["hits"]:
                hit_dict = {}
                if "title" in hit["_source"]:
                     hit_dict["title"] = "".join(hit["_source"]["title"])

                if "content" in hit["_source"]:
                    hit_dict["content"] = hit["_source"]["content"][:500]
                else:
                    hit_dict["content"] = hit["_source"]["job_desc"][:500]

                hit_dict["url"] = hit["_source"]["url"]
                hit_dict["score"] = hit["_score"]
                hit_list.append(hit_dict)
        else:
            for hit in response["hits"]["hits"]:
                hit_dict = {}
                if "title" in hit["highlight"]:
                    hit_dict["title"] = "".join(hit["highlight"]["title"])
                else:
                    if "title" in hit["_source"]:
                        hit_dict["title"] = "".join(hit["_source"]["title"])

                if "content" in hit["highlight"]:
                    hit_dict["content"] = "".join(hit["highlight"]["content"])[:500]
                else:
                    if "content" in hit["_source"]:
                        hit_dict["content"] = hit["_source"]["content"][:500]
                    else:
                        hit_dict["content"] = hit["_source"]["job_desc"][:500]

                hit_dict["url"] = hit["_source"]["url"]
                hit_dict["score"] = hit["_score"]
                hit_list.append(hit_dict)
        return render(request, "result.html",{"page":page, "all_hits":hit_list, "key_words":key_words, "total_nums":total_nums, "page_nums":page_nums, "last_seconds":last_secondes, "jobbole_count":jobbole_count, "zhihu_count":zhihu_count, "lagou_count":lagou_count, "topn_search":topn_search, "date_type":date_type})

    def get_response(self, date_type, key_words, page):
        if date_type == "article":
            index = "jobbole"
            doc_type = "article"
            content = "content"
        if date_type == "question":
            index = "zhihu"
            doc_type = "zhihu_question"
            content = "content"
        if date_type == "job":
            index = "lagou"
            doc_type = "job"
            content = "job_desc"
        response = client.search(
            index=index,
            doc_type=doc_type,
            body={
                "query": {
                    "multi_match": {
                        "query": key_words,
                        "fields": ["title", content]
                    }
                },
                "from": page * 10,
                "size": 10,
                "highlight": {
                    "pre_tags": ['<span class="keyWord">'],
                    "post_tags": ['</span>'],
                    "fields": {
                        "title": {},
                        "content": {},
                    }
                }
            }
        )
        return response



