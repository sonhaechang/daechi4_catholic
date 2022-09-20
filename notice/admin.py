from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from notice.forms import NoticeForm
from notice.models import Notice, Comment


# Register your models here.
@admin.register(Notice)
class notice(SummernoteModelAdmin):
	# summernote_fields = ('content',)
	form = NoticeForm
	list_display = ['user', 'title', 'created_at', 'updated_at']
	list_filter = ['created_at', 'updated_at']
	raw_id_fields =['user']
	readonly_fields = ['hits']
	search_fields = ['user__username', 'title', 'content']
	ordering = ['-updated_at', '-created_at']
	


@admin.register(Comment)
class noticecomment(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at', 'updated_at']