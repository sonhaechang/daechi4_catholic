# from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView


class BasePostDetail(DetailView):
	'''  Post Detail을 확인하는 모든 DetailView에서 상속 받아서 사용할 Base DetailView '''

	model = None
	form_class = None
	app_name = None

	def get_objects(self):
		''' pk로 queryset을 filtering 후 object을 반환 '''

		return get_object_or_404(
			self.model.objects.select_related('user'), pk=self.kwargs['pk'])

	def get_template_names(self):
		''' app_name을 이용해서 templates 반환 '''

		app_name = self.app_name
		return [f'{app_name}/container/{app_name}_detail.html']

	def hit_count(self):
		''' 해당 object의 조회수를 1개씩 증가시킴 '''

		obj = self.get_objects()

		# hit_count_{pk}라는 session이 True일때만 해당 query의 hits를 + 1 증가해서 update후 해당 세션 False로 변경
		if self.request.session.get(f'hit_count_{self.kwargs["pk"]}', True):
			obj.hits = obj.hits + 1
			obj.save()
			self.request.session[f'hit_count_{self.kwargs["pk"]}'] = False

	def get_context_data(self, **kwargs):
		''' templates에서 사용할 변수들을 dict로 넘기는 함수 '''

		context = super().get_context_data(**kwargs)
		obj = self.get_objects()
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