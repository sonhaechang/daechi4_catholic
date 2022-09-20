from django.contrib import admin
from flower.models import Flower, Thumbnail, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Flower)
class Flower(SummernoteModelAdmin):
    # summernote_fields = ('content',)
    list_display = ['id', 'user', 'title', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'user']
    raw_id_fields =['user']
    readonly_fields = ['hits']
    search_fields = ['content', 'created_at']
    ordering = ['-updated_at', '-created_at']


@admin.register(Thumbnail)
class Thumbnail(admin.ModelAdmin):
    list_display = ['id', 'flower', 'thumbnail']


@admin.register(Comment)
class flowercomment(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at', 'updated_at']
