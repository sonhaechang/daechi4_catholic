from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from video.models import Video, Comment


# Register your models here.
@admin.register(Video)
class Video(SummernoteModelAdmin):
    list_display = ['user', 'title', 'created_at', 'updated_at']
    raw_id_fields =['user']
    list_filter = ['created_at', 'updated_at', 'user']
    search_fields = ['content', 'created_at']
    ordering = ['-created_at']


@admin.register(Comment)
class comment(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at', 'updated_at']