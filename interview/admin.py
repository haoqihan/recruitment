from django.contrib import admin
from django.http import HttpResponse

from interview.models import Candidate
from datetime import datetime
import csv

exportable_fields = (
    'username', 'city', 'phone', 'bachelor_school', 'master_school', 'degree', 'first_result', 'first_interview_user',
    'second_result', 'second_interview_user', 'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer_user')


# 导出excel
def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=%s-list-%s.csv' % (
        'recruitment-candidates',
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )
    # 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list],
    )

    for obj in queryset:
        # 单行 的记录（各个字段的值）， 根据字段对象，从当前实例 (obj) 中获取字段值
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)

    return response


# 定义名称
export_model_as_csv.short_description = u'导出为CSV文件'


class CandidateAdmin(admin.ModelAdmin):
    actions = (export_model_as_csv,)
    # 不显示的内容
    exclude = ("creator", "created_date", "modified_date")
    # 列表要显示的内容
    list_display = (
        'username', 'city', 'bachelor_school', 'first_score', 'first_result', 'second_score', 'second_result',
        'hr_score', 'hr_result'
    )
    # 增加和修改的字段结构
    fieldsets = (
        (None, {"fields": (
            "userid",
            ("username", "city"),
            ("phone", "email"),
            ("apply_position", "born_address"),
            ("gender", "candidate_remark"),
            ("bachelor_school", "master_school", "doctor_school"),
            ("major", "degree"),
            "test_score_of_general_ability", "paper_score", "last_editor")}
         ),
        ("第一轮面试记录", {"fields": (
            ("first_score", "first_learning_ability"),
            "first_advantage", "first_disadvantage",
            "first_result", "first_interview_user", "first_recommend_position", "first_remark")}
         ),
        ("第二轮面试记录", {"fields": (
            ("second_score", "second_learning_ability"),
            ("second_professional_competency", "second_pursue_of_excellence"),
            ("second_communication_ability", "second_pressure_score"),
            "second_advantage", "second_disadvantage", "second_result", "second_interview_user",
            "second_recommend_position",
            "second_remark")}),
        ("第三轮面试记录", {"fields": (
            ("hr_score", "hr_responsibility"),
            ("hr_communication_ability", "hr_logic_ability"),
            ("hr_potential", "hr_stability"),
            "hr_advantage", "hr_disadvantage", "hr_result", "hr_interviewer_user", "hr_remark")}),
    )
    # 搜索的字段
    search_fields = ["username", "phone", "email", "bachelor_school"]
    # 右侧筛选条件
    list_filter = ["city", "first_result", "second_result", "hr_result", "first_interview_user",
                   'second_interview_user', 'hr_interviewer_user']
    # 列表页排序字段
    ordering = ('hr_result', "second_result", "first_result")


admin.site.register(Candidate, CandidateAdmin)
"""
启动open ldap
docker run -p 389:389 -p 636:636 --name my-openldap-container --env LDAP_ORGANISATION="ihopeit" --env LDAP_DOMAIN="ihopeit.com"  --env LDAP_ADMIN_PASSWORD="admin_password_4_ldap" --detach osixia/openldap:1.4.0
docker run -dit \
-p 389:389 \
-v /data/ldap/ldap:/var/lib/ldap \
-v /data/ldap/slapd.d:/etc/ldap/slapd.d \
--name ldap \
--env LDAP_TLS=false \
--env LDAP_ORGANISATION="pibigstar" \
--env LDAP_DOMAIN="pibigstar.com" \
--env LDAP_ADMIN_PASSWORD="123456" \
--env LDAP_CONFIG_PASSWORD="123456" \
--restart always \
--detach osixia/openldap

配置LDAP组织者：LDAP_ORGANISATION
配置LDAP域：LDAP_DOMAIN
配置LDAP密码：LDAP_ADMIN_PASSWORD
默认登录用户名：admin



docker run -p 80:80 -p 443:443 --name phpldapadmin-service --hostname phpldapadmin-service --link my-openldap-container:ldap-host --env PHPLDAPADMIN_LDAP_HOSTS=ldap-host --detach osixia/phpldapadmin:0.9.0






# 安装相关模块
pip install django-python3-ldap







静，稳
"""
