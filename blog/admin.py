from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin

from .models import Category, Blog, Tag, Comment

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def image_show(self,obj):
        if obj.image:
            return format_html(f"<img src = '{obj.image.url}' width='50px'>")
        return None

    def count_blog(self,obj):
        return obj.blog_set.count()


    list_display = ('name','slug','count_blog','image_show')
    readonly_fields = ('slug',)
    search_fields = ('name',)


@admin.action(description="Custom delete delets tags")
def custom_delete_tags(modeladmin,request,queryset):
    queryset.update(is_deleted = True)

@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("name",'is_deleted')
    actions = [custom_delete_tags]


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("name","is_deleted")
    actions = [custom_delete_tags]
