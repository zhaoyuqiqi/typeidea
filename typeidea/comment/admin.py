from django.contrib import admin

# Register your models here.
from typeidea.custom_site import custom_site
from .models import Comment


@admin.register(Comment ,site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'target','nickname','content','website','create_time'
    )