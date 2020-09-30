#-*- coding = utf-8 -*-
#@Time : 2020/9/30 20:49
#@Author : 赵玉琦
#@software : PyCharm
from django import forms
class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea,label='摘要',required=False)