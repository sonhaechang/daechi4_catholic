from django.views.generic import ListView

from core.base_views.pagination import default_pagination
from school.models import School_Class

class BasePostList(ListView):
	model = None
	app_name = None
	paginate_by = None

	def get_template_names(self):
		app_name = self.app_name
		return [f'{app_name}/container/{app_name}_list.html']

	def get_q_params(self):
		return self.request.GET.get('q', '')

	def get_queryset(self):
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
		context = super().get_context_data(**kwargs)
		queryset = self.get_queryset()
		app_name = self.app_name

		context['total_len'] = len(queryset)
		context['app_name'] = app_name
		context['q'] = self.get_q_params()

		if app_name  == 'gallery' or app_name  == 'picture' or app_name  == 'flower':
			context['show_type'] = self.request.GET.get('show_type', 'card')
		else:
			context['show_type'] = self.request.GET.get('show_type', 'list')
		
		if app_name == 'school' and self.kwargs['school_class']:
			context['school_class'] = self.kwargs['school_class']
			context['school_classs'] = School_Class.objects.all()

		context.update(default_pagination(self.request, queryset, self.paginate_by))

		return context