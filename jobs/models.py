from django.db import models
from django.contrib.auth.models import User

# 候选人学历
DEGREE_TYPE = (('本科', '本科'), ('硕士', '硕士'), ('博士', '博士'))

# Create your models here.
JobTypes = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
    (3, "设计类")

]
Cities = [
    (0, "北京"),
    (1, "上海"),
    (2, "深圳")
]


class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name="职位类别")
    job_name = models.CharField(max_length=255, blank=False, verbose_name="职位名称")
    job_city = models.SmallIntegerField(blank=False, choices=Cities, verbose_name="工作地点")
    job_responsibility = models.TextField(max_length=1024, verbose_name="职位职责")
    job_requirement = models.TextField(max_length=1024, verbose_name="职位要求")
    creator = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    class Meta:
        verbose_name = "招聘信息"
        verbose_name_plural = verbose_name
