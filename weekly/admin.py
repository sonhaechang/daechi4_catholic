from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from weekly.models import Weekly, Comment


# Register your models here.
@admin.register(Weekly)
class weekly(SummernoteModelAdmin):
    list_display = ['user', 'title', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'user']
    raw_id_fields =['user']
    readonly_fields = ['hits']
    search_fields = ['content', 'created_at']
    ordering = ['-created_at']


@admin.register(Comment)
class weeklycomment(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at', 'updated_at']