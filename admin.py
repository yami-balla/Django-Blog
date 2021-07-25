from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post
# Register your models here.

admin.site.site_header='Blog Admin'

class BlogAdmin(admin.ModelAdmin):
    list_display =['Title', 'Slug', 'Status', 'Created_on']
    list_filter =['Status',]
    search_fields=('Title',)
    prepopulated_fields={'Slug':('Title',)}

admin.site.register(Post, BlogAdmin)
admin.site.unregister(Group)