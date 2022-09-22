from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import Value as V
from django.db.models.functions import Concat

from accounts.models import Profile


# Register your models here.
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


@admin.register(Profile)
class profile(admin.ModelAdmin):
    list_display = ['id', 'user']


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_search_results(self, request, queryset, search_term):
        ''' 
            get_search_results override 
            get_search_results는 admin에서 search_fields 검색 기능 
            fullname으로 이름 검색 가능하게 필터링
        '''

        queryset, may_have_duplicates = super().get_search_results(
            request, queryset, search_term,
        )

        queryset |= self.model.objects.annotate(full_name=Concat('last_name', V(''), 'first_name')).filter(   
            Q(full_name__icontains=search_term) | 
            Q(first_name__icontains=search_term) | 
            Q(last_name__icontains=search_term)
        )

        return queryset, may_have_duplicates

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
