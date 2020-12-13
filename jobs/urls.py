from django.conf.urls import url
from jobs.views import jobList
from jobs.views import detail

urlpatterns = [
    # 职位列表
    url(r'^joblist/', view=jobList, name="jonList"),
    url(r'^job/(?P<job_id>\d+)/$', view=detail, name="detail")
]
