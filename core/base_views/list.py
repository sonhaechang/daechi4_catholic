from django.views.generic import ListView

from core.base_views.pagination import default_pagination
from school.models import School_Class

class BasePostList(ListView):
	''' Post를 조회하는 모든  ListView에서 상속 받아서 사용할 Base ListView '''

	model = None
	app_name = None
	paginate_by = None

	def get_template_names(self):
		''' app_name을 이용해서 template name을 반환 '''
		
		app_name = self.app_name
		return [f'{app_name}/container/{app_name}_list.html']

	def get_q_params(self):
		''' 검색된 query paramter를 get으로 받아와 반환'''

		return self.request.GET.get('q', '')

	def get_queryset(self):
		''' 조건에 맞는 queryset을 반환 '''

		app_name = self.app_name
		queryset = self.model.objects.all().prefetch_related(
			'comment_set').select_related('user').order_by('-created_at')

		if app_name  == 'gallery' or app_name  == 'picture' \
				or app_name  == 'flower' or app_name  == 'school':
			queryset = queryset.prefetch_related('thumbnail_set')

			if app_name  == 'school':
				school_class = self.kwargs['school_class']
				queryset = queryset.filter(school_class__name=school_class).select_related('school_class')

		return queryset.filter(title__icontains=self.get_q_params()) \
				if self.get_q_params() else queryset

	def get_context_data(self, **kwargs):
		''' templates에서 사용할 변수들을 dict로 넘기는 함수 '''

		context = super().get_context_data(**kwargs)
		queryset = self.get_queryset()
		app_name = self.app_name

		context['total_len'] = len(queryset)
		context['app_name'] = app_name
		context['q'] = self.get_q_params()

		if app_name  == 'gallery' or app_name  == 'picture' or app_name  == 'flower':
			context['show_type'] = self.request.GET.get('show_type', 'card') # default 값으로 'card' 설정
		else:
			context['show_type'] = self.request.GET.get('show_type', 'list') # default 값으로 'list' 설정
		
		if app_name == 'school' and self.kwargs['school_class']:
			context['school_class'] = self.kwargs['school_class']
			context['school_classs'] = School_Class.objects.all()

		context.update(default_pagination(self.request, queryset, self.paginate_by)) # pagination 처리

		return context