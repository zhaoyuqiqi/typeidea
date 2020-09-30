#-*- coding = utf-8 -*-
#@Time : 2020/10/1 1:10
#@Author : 赵玉琦
#@software : PyCharm
from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    用来自动补充这些Model的 owner 字段
    针对queryset 过滤当前用户数据
    """
    exclude = ('owner',)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)