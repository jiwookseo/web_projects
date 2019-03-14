from django.contrib import admin
from .models import Posting, Comment


class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('id', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'content')


class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('id', 'content', 'created_at', 'updated_at')
    list_display_links = ('id', 'content')


admin.site.register(Posting, PostingModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
