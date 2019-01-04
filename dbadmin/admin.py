# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from dbadmin.models import DjangoAdminLog
from dbadmin.models import DjangoContentType
from dbadmin.models import DjangoMigrations
from dbadmin.models import DjangoSession
from dbadmin.models import ZhihuQuestion
from dbadmin.models import JobboleArticle
from dbadmin.models import LagouJob
from dbadmin.models import ProxyIp
from dbadmin.models import ZhihuAnswer



# Register your models here.
class LagouJobAdmin(admin.ModelAdmin):
    list_display = ('url', 'url_object_id', 'title', 'salary', 'job_city', 'work_years', 'degree_need', 'job_type', 'pulish_time', 'tags', 'job_advantage', 'job_addr', 'company_url', 'company_name', 'crawl_time', 'crawl_update_time')
    list_per_page = 10
    list_filter = ('crawl_time', 'crawl_update_time')
    search_fields = ('url', 'url_object_id', 'title', 'salary', 'job_city', 'work_years', 'degree_need', 'job_type', 'pulish_time', 'tags', 'job_advantage', 'job_addr', 'company_url', 'company_name', 'crawl_time', 'crawl_update_time')
admin.site.register(LagouJob, LagouJobAdmin)
class DjangoAdminLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'action_time', 'object_id', 'object_repr', 'action_flag', 'change_message', 'content_type_id', 'user_id')
    list_per_page = 10
    list_filter = ('action_time', 'user_id')
    search_fields = ('id', 'action_time', 'object_id', 'object_repr', 'action_flag', 'change_message', 'content_type_id', 'user_id')
admin.site.register(DjangoAdminLog, DjangoAdminLogAdmin)
class DjangoContentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_label', 'model')
    list_per_page = 10
    search_fields = ('id', 'app_label', 'model')
admin.site.register(DjangoContentType, DjangoContentTypeAdmin)
class DjangoMigrationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'app', 'name', 'applied')
    list_per_page = 10
    search_fields = ('id', 'app', 'name', 'applied')
admin.site.register(DjangoMigrations, DjangoMigrationsAdmin)
class DjangoSessionAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'session_data', 'expire_date')
    list_per_page = 10
    search_fields = ('session_key', 'session_data', 'expire_date')
admin.site.register(DjangoSession, DjangoSessionAdmin)
class JobboleArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_date', 'url', 'url_object_id', 'front_image_url', 'front_image_path', 'comment_nums', 'fav_nums', 'praise_nums', 'tags')
    list_per_page = 10
    list_filter = ('create_date', 'tags')
    search_fields = ('title', 'create_date', 'url', 'url_object_id', 'front_image_url', 'front_image_path', 'comment_nums', 'fav_nums', 'praise_nums', 'tags')
admin.site.register(JobboleArticle, JobboleArticleAdmin)
class ProxyIpAdmin(admin.ModelAdmin):
    list_display = ('ip', 'port', 'speed', 'proxy_type')
    list_per_page = 10
    list_filter = ('port', 'proxy_type')
    search_fields = ('ip', 'port', 'speed', 'proxy_type')
admin.site.register(ProxyIp, ProxyIpAdmin)
class ZhihuAnswerAdmin(admin.ModelAdmin):
    list_display = ('zhihu_id', 'url', 'question_id', 'author_id', 'praise_num', 'comments_num', 'create_time', 'update_time', 'crawl_time', 'crawl_update_time')
    list_per_page = 10
    list_filter = ('update_time', 'crawl_time', 'crawl_update_time')
    search_fields = ('zhihu_id', 'url', 'question_id', 'author_id', 'praise_num', 'comments_num', 'create_time', 'update_time', 'crawl_time', 'crawl_update_time')
admin.site.register(ZhihuAnswer, ZhihuAnswerAdmin)
class ZhihuQuestionAdmin(admin.ModelAdmin):
    list_display = ('zhihu_id', 'topics', 'url', 'title', 'create_time', 'update_time', 'answer_num', 'comments_num', 'watch_user_num', 'click_num', 'crawl_time', 'crawl_update_time')
    list_per_page = 10
    list_filter = ('update_time', 'crawl_time', 'crawl_update_time')
    search_fields = ('zhihu_id', 'topics', 'url', 'title', 'content', 'create_time', 'update_time', 'answer_num', 'comments_num', 'watch_user_num', 'click_num', 'crawl_time', 'crawl_update_time')
admin.site.register(ZhihuQuestion, ZhihuQuestionAdmin)
admin.site.site_header = 'ZHW搜索引擎 后台管理'
admin.site.site_title = 'ZHW后台搜索引擎'