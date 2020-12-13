from django.contrib import admin
from jobs.models import Job


# Register your models here.
class JobAdmin(admin.ModelAdmin):
    # 显示那些信息
    list_display = ['job_name', 'job_type', 'job_city', 'creator', 'create_date', 'modified_date']
    # 隐藏那些信息
    exclude = ['creator', 'create_date', 'modified_date']

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Job, JobAdmin)
