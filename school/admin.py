from django.contrib import admin
from school.models import School_Class, School, UploadFile, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class UploadFileInline(admin.TabularInline):
    model = UploadFile
    raw_id_fields = ['post']
    fields = ['post', 'upload_file']
    extra = 0


@admin.register(School)
class School(SummernoteModelAdmin):
    list_display = ['user', 'title', 'created_at', 'updated_at']
    raw_id_fields =['user']
    list_filter = ['created_at', 'updated_at', 'school_class']
    search_fields = ['content', 'created_at']
    ordering = ['-created_at']
    inlines = [UploadFileInline]


@admin.register(School_Class)
class SchoolClass(SummernoteModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


@admin.register(Comment)
class comment(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at', 'updated_at']