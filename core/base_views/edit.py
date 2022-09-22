from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.translation import gettext_lazy as _

from django.views import View
from django.views.generic.base import ContextMixin


class PostFormMixin(ContextMixin):
	''' requests에서 양식을 표시하고 처리하는 방법을 제공하는 Mixin '''

	initial = {}
	prefix = None

	def get_form(self, form_class):
		''' View에서 사용할 form class를 반환 '''

		return form_class(**self.get_form_kwargs())

	def get_form_kwargs(self):
		''' form에 instance의 키워드 인자를 반환 '''

		kwargs = {"initial": self.initial, "prefix": self.prefix}

		if self.request.method in ("POST", "PUT"):
			kwargs.update({"data": self.request.POST, "files": self.request.FILES})

		if hasattr(self, "get_object"):
			kwargs.update({"instance": self.get_object()})

		return kwargs

	def get_redirect_url(self):
		''' app_name을 이용해서 redirect url을 생성해서 반환 '''

		return f'{self.app_name}:{self.app_name}_detail'


class PostProcessView(PostFormMixin, View):
	''' form에서 GET, POST 요청을 처리하는 View '''

	def post_save(self, post, upload_file=None):
		''' 개시글을 저장, 수정하는 함수 '''

		school_class = self.kwargs['school_class'] if self.app_name  == 'school' else None
		redirect_url = self.get_redirect_url()

		if school_class is not None and self.post_method == 'CREATE':
			post.school_class = self.models['post_model'].objects.get(name=school_class)

		post.user = self.request.user
		post.save()

		self.upload_file(post)

		# upload file이 있을 때만 delete_file 함수 실행
		if upload_file is not None:
			self.delete_file(upload_file)

		message = _('포스팅을 생성했습니다.') if self.post_method == 'CREATE' else _('포스팅을 수정했습니다.')
		messages.success(self.request, message)

		if school_class:
			return redirect(redirect_url, school_class=school_class, pk=post.pk)
		return redirect(redirect_url, pk=post.pk)

	def upload_file(self, post):
		''' upload file이 있으면 저장하는 함수 '''

		for f in self.request.FILES.getlist('upload_file'):
			self.models['upload_model'].objects.create(post=post, upload_file=f)

	def delete_file(self, upload_file):
		''' 
		upload된 file을 삭제하는 함수 
		UPDATE일때만 함수가 실행
		'''

		for f in self.request.POST.getlist("delete_file"):
			p = upload_file.get(pk=f)
			p.delete()

	def get_context_data(self, **kwargs):
		''' templates에서 사용할 변수들을 dict로 넘기는 함수 '''

		context = dict()

		context['app_name'] = self.app_name
		context['form'] = self.get_form(self.form_class)

		# object가 있고 (GET, POST(UPDATE 일때)) uplooad file이 있을때  upload file 전부 가져옴
		if hasattr(self, 'get_object') and hasattr(self.get_object(), 'uploadfile_set'):
			context['upload_file'] = self.get_object().uploadfile_set.all()

		if self.app_name == 'school' and self.kwargs['school_class']:
			context['school_class'] = self.kwargs['school_class']

		return context

	def get(self, request, *args, **kwargs):
		''' GET 요청을 처리하는 함수 '''

		kwargs = self.get_context_data(**kwargs)
		return render(request, self.get_template_names(), kwargs)

	def post(self, request, *args, **kwargs):
		''' POST 요청을 처리하는 함수 '''

		kwargs = self.get_context_data(**kwargs)

		if kwargs['form'].is_valid():
			if self.post_method == 'UPDATE':
				return self.post_save(
					kwargs['form'].save(commit=False), kwargs['upload_file'])
			else:
				return self.post_save(kwargs['form'].save(commit=False))
		
		return render(request, self.get_template_names(), kwargs)

	
class BasePostCreate(LoginRequiredMixin, PermissionRequiredMixin, PostProcessView):
	''' Post를 생성하는 모든 CreateView에서 상속 받아서 사용할 Base CreateView '''

	models = {}
	app_name = None
	form_class = None
	raise_exception = True
	permission_required = None
	post_method = 'CREATE'

	def get_template_names(self):
		''' app_name을 이용해서 template name을 반환 '''

		app_name = self.app_name
		return [f'{app_name}/container/{app_name}_create.html']


class BasePostEdit(LoginRequiredMixin, PermissionRequiredMixin, PostProcessView):
	''' Post를 수정하는 모든  EditView에서 상속 받아서 사용할 Base EditView '''

	models = {}
	app_name = None
	form_class = None
	permission_required = None
	post_method = 'UPDATE'

	def get_template_names(self):
		''' app_name을 이용해서 template name을 반환 '''

		app_name = self.app_name
		return [f'{app_name}/container/{app_name}_edit.html']

	def get_object(self):
		''' pk로 queryset을 filtering 후 object을 반환 '''

		obj = get_object_or_404(
			self.models['post_model'], pk=self.kwargs['pk'])
		return obj if obj.user == self.request.user else PermissionDenied()