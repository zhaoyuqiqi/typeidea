from django.contrib import admin
from django.urls import reverse
from django.utils.html import mark_safe
# from django.utils.safestring import mark_safe
from blog.adminforms import PostAdminForm
from blog.models import Category, Post, Tag


# Register your models here.
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site


class PostInline(admin.TabularInline):
    fields = ('title','desc')
    extra = 1  #界面初始的时候有几个
    model = Post

@admin.register(Category,site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'create_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    inlines = [PostInline]

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag ,site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'create_time', 'owner')
    fields = ('name', 'status')


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器 只显示当前账户的用户分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category__id=category_id)
        return queryset


@admin.register(Post ,site=custom_site)
class PostAdmin(BaseOwnerAdmin):

    form = PostAdminForm

    list_display = [
        'title', 'category', 'status',
        'create_time', 'owner', 'operator',
    ]
    list_display_links = []
    list_filter = [CategoryOwnerFilter]
    search_fields = [
        'title', 'category__name'
    ]
    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True


    # 编辑页面

    exclude = ('owner',)

    # 编辑界面设置
    fieldsets = (
        ('基础配置',{
            'description':'基础配置描述',
            'fields':(
                ('category', 'title'),
                'status',
            ),
        }),
        ('内容',{
            'fields':(
                'desc',
                'content',
            ),
        }),
        ('额外信息',{
            'classes':('collapse'),
            'fields':('tag',),
        })
    )

    # 编辑界面设置
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )


    # 标签的过滤器
    # filter_horizontal = ('tag',)
    #
    # filter_vertical = ('tag',)

    def operator(self, obj):
        url = reverse('cus_admin:blog_post_change', args=(obj.id,))
        return mark_safe(f'<a href = "{url}">编辑</a>')

        # 下面的函数有问题
        # return format_html(
        #     '<a href = "{ }">编辑</a>',
        #     reverse('admin:blog_post_change', args=(obj.id,))
        # )

    operator.short_description = '操作'

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner = request.user)

    class Media:
        css = {
            "all":('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css')
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js')