# from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView

# from core.base_views.pagination import base_pagination


class BasePostDetail(DetailView):
	model = None
	form_class = None
	app_name = None

	def get_objects(self):
		return get_object_or_404(
			self.model.objects.select_related('user'), pk=self.kwargs['pk'])

	def get_template_names(self):
		app_name = self.app_name

		# if self.request.is_ajax():
		# 	return ['base_content/comment_form_ajax.html']
		return [f'{app_name}/container/{app_name}_detail.html']

	def hit_count(self):
		queryset = self.get_objects()

		if self.request.session.get('hit_count_%s' % self.kwargs['pk'], True):
			queryset.hits = queryset.hits + 1
			queryset.save()
			self.request.session['hit_count_%s' % self.kwargs['pk']] = False

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		obj = self.get_objects()
		# comments = obj.comment_set.all().order_by('-id')
		# comments_count = comments.count()

		# paginator = Paginator(comments.filter(parent__isnull=True), 5)
		# comments = base_pagination(request=self.request, paginator=paginator)

		# context['comments'] = comments
		# context['comment_count'] = comments_count

		app_name = self.app_name

		context['form'] = self.form_class
		context['obj'] = obj
		context['app_name'] = app_name

		comment_url = f'{app_name}:{app_name}_comment'

		if app_name == 'school':
			context['comment_url'] = reverse(comment_url, kwargs={
				'post_pk': self.kwargs['pk'],
				'school_class': self.kwargs['school_class']
			})
		else:
			context['comment_url'] = reverse(comment_url, kwargs={'post_pk': self.kwargs['pk']})

		if hasattr(context['obj'], 'uploadfile_set'):
			context['file_count'] = context['obj'].uploadfile_set.all().count()

		self.hit_count()

		return context