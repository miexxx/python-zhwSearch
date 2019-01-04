# encoding: utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField(verbose_name='操作时间')
    object_id = models.TextField(blank=True, null=True, verbose_name='加密id')
    object_repr = models.CharField(max_length=200, verbose_name='操作效果')
    action_flag = models.SmallIntegerField(verbose_name='操作标志')
    change_message = models.TextField(verbose_name='操作消息')
    content_type_id = models.IntegerField(blank=True, null=True, verbose_name='操作类型id')
    user_id = models.IntegerField(verbose_name='用户编号')

    class Meta:
        managed = False
        db_table = 'django_admin_log'
        verbose_name = '日志管理'
        verbose_name_plural = "日志管理"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, verbose_name='应用模块')
    model = models.CharField(max_length=100, verbose_name='应用模型')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        verbose_name = '应用模块管理'
        verbose_name_plural = "应用模块管理"
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, verbose_name='应用模块')
    name = models.CharField(max_length=255, verbose_name='标题')
    applied = models.DateTimeField(verbose_name='操作完成时间')

    class Meta:
        managed = False
        verbose_name = '迁移文件管理'
        verbose_name_plural = "迁移文件管理"
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField(verbose_name='过期时间')

    class Meta:
        managed = False
        verbose_name = 'session管理'
        verbose_name_plural = "session管理"
        db_table = 'django_session'


class JobboleArticle(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name='文章标题')
    create_date = models.DateField(blank=True, null=True, verbose_name='发布日期')
    url = models.CharField(max_length=300, blank=True, null=True, verbose_name='url地址')
    url_object_id = models.CharField(primary_key=True, max_length=50, verbose_name='加密后的url地址')
    front_image_url = models.CharField(max_length=300, blank=True, null=True, verbose_name='图片来源地址')
    front_image_path = models.CharField(max_length=300, blank=True, null=True, verbose_name='图片存取地址')
    comment_nums = models.IntegerField(blank=True, null=True, verbose_name='评论数量')
    fav_nums = models.IntegerField(verbose_name='点赞数量')
    praise_nums = models.IntegerField(verbose_name='关注数量')
    tags = models.CharField(max_length=200, verbose_name='标签')
    content = models.TextField(blank=True, null=True, verbose_name='文章内容')

    class Meta:
        managed = False
        verbose_name = '伯乐网管理'
        verbose_name_plural = "伯乐网管理"
        db_table = 'jobbole_article'


class LagouJob(models.Model):
    url = models.CharField(max_length=300, verbose_name='来源url')
    url_object_id = models.CharField(primary_key=True, max_length=50, verbose_name='来源url加密')
    title = models.CharField(max_length=100,  verbose_name='标题')
    salary = models.CharField(max_length=20, blank=True, null=True,  verbose_name='薪资')
    job_city = models.CharField(max_length=10, blank=True, null=True, verbose_name='工作城市')
    work_years = models.CharField(max_length=100, blank=True, null=True, verbose_name='工作经验')
    degree_need = models.CharField(max_length=30, blank=True, null=True, verbose_name='职位需求')
    job_type = models.CharField(max_length=20, blank=True, null=True, verbose_name='工作类型')
    pulish_time = models.CharField(max_length=20, verbose_name='发布时间')
    tags = models.CharField(max_length=100, blank=True, null=True, verbose_name='标签')
    job_advantage = models.CharField(max_length=1000, blank=True, null=True, verbose_name='工作待遇')
    job_desc = models.TextField(verbose_name='工作描述')
    job_addr = models.CharField(max_length=50, blank=True, null=True, verbose_name='工作地点')
    company_url = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司官网')
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司名称')
    crawl_time = models.DateTimeField(blank=True, null=True, verbose_name='爬取时间')
    crawl_update_time = models.DateTimeField(blank=True, null=True, verbose_name='更新数据时间')

    class Meta:
        managed = False
        verbose_name = "拉钩网管理"
        verbose_name_plural = "拉钩网管理"
        db_table = 'lagou_job'


class ProxyIp(models.Model):
    ip = models.CharField(primary_key=True, max_length=255, verbose_name='代理ip')
    port = models.CharField(max_length=255, blank=True, null=True, verbose_name='端口号')
    speed = models.IntegerField(blank=True, null=True, verbose_name='网速')
    proxy_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='ip类型')

    class Meta:
        managed = False
        db_table = 'proxy_ip'
        verbose_name = '代理ip管理'
        verbose_name_plural = "代理ip管理"



class ZhihuAnswer(models.Model):
    zhihu_id = models.BigIntegerField(primary_key=True, verbose_name='知乎回答id')
    url = models.CharField(max_length=300, verbose_name='知乎回答url')
    question_id = models.BigIntegerField(verbose_name='知乎问题id')
    author_id = models.CharField(max_length=100, blank=True, null=True, verbose_name='回复人id')
    content = models.TextField(verbose_name='回复内容')
    praise_num = models.IntegerField(verbose_name='分享数')
    comments_num = models.IntegerField(verbose_name='评论数')
    create_time = models.DateTimeField(verbose_name='回答时间')
    update_time = models.DateTimeField(verbose_name='更新时间')
    crawl_time = models.DateTimeField(verbose_name='爬取时间')
    crawl_update_time = models.DateTimeField(verbose_name='重新爬取时间')

    class Meta:
        managed = False
        db_table = 'zhihu_answer'
        verbose_name = '知乎回答管理'
        verbose_name_plural = "知乎回答管理"


class ZhihuQuestion(models.Model):
    zhihu_id = models.BigIntegerField(primary_key=True, verbose_name='知乎提问id')
    topics = models.CharField(max_length=255, blank=True, null=True, verbose_name='标签')
    url = models.CharField(max_length=300, verbose_name='问题地址')
    title = models.CharField(max_length=255, verbose_name='问题标题')
    content = models.TextField(verbose_name='问题内容')
    create_time = models.DateTimeField(blank=True, null=True, verbose_name='提问时间')
    update_time = models.DateTimeField(blank=True, null=True, verbose_name='更新时间')
    answer_num = models.IntegerField(verbose_name='回答数')
    comments_num = models.IntegerField(verbose_name='评论数')
    watch_user_num = models.IntegerField(verbose_name='观看数')
    click_num = models.IntegerField(verbose_name='点击数')
    crawl_time = models.DateTimeField(verbose_name='爬取时间')
    crawl_update_time = models.DateTimeField(blank=True, null=True, verbose_name='重新爬取时间')

    class Meta:
        managed = False
        db_table = 'zhihu_question'
        verbose_name = '知乎提问管理'
        verbose_name_plural = '知乎提问管理'
