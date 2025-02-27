from django.contrib import admin
from .models import *


admin.site.register(AboutPage)
admin.site.register(ContactPage)
admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','content','created_at','email']
    list_filter = ['created_at']
    search_fields = ['name','content','email']