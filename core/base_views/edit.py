from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.translation import gettext_lazy as _

from django.views import View
from django.views.generic.base import ContextMixin


class PostFormMixin(ContextMixin):
	initial = {}
	prefix = None

	def get_form(self, form_class):
		return form_class(**self.get_form_kwargs())

	def get_form_kwargs(self):
		kwargs = {"initial": self.initial, "prefix": self.prefix}

		if self.request.method in ("POST", "PUT"):
			kwargs.update({"data": self.request.POST, "files": self.request.FILES})

		if hasattr(self, "get_object"):
			kwargs.update({"instance": self.get_object()})

		return kwargs

	def get_redirect_url(self):
		return f'{self.app_name}:{self.app_name}_detail'


class PostProcessView(PostFormMixin, View):
	def post_save(self, post, upload_file=None):
		school_class = self.kwargs['school_class'] if self.app_name  == 'school' else None
		redirect_url = self.get_redirect_url()

		# if hasattr(post, 'school_class'):
		if school_class is not None and self.post_method == 'CREATE':
			post.school_class = self.models['post_model'].objects.get(name=school_class)

		post.user = self.request.user
		post.save()

		self.upload_file(post)

		if upload_file is not None:
			self.delete_file(upload_file)

		message = _('포스팅을 생성했습니다.') if self.post_method == 'CREATE' else _('포스팅을 수정했습니다.')
		messages.success(self.request, message)

		if school_class:
			return redirect(redirect_url, school_class=school_class, pk=post.pk)
		return redirect(redirect_url, pk=post.pk)

	def upload_file(self, post):
		for f in self.request.FILES.getlist('upload_file'):
			self.models['upload_model'].objects.create(post=post, upload_file=f)

	def delete_file(self, upload_file):
		for f in self.request.POST.getlist("delete_file"):
			p = upload_file.get(pk=f)
			p.delete()

	def get_context_data(self, **kwargs):
		context = dict()

		context['app_name'] = self.app_name
		context['form'] = self.get_form(self.form_class)

		if hasattr(self, 'get_object') and hasattr(self.get_object(), 'uploadfile_set'):
			context['upload_file'] = self.get_object().uploadfile_set.all()

		if self.app_name == 'school' and self.kwargs['school_class']:
			context['school_class'] = self.kwargs['school_class']

		return context

	def get(self, request, *args, **kwargs):
		kwargs = self.get_context_data(**kwargs)
		return render(request, self.get_template_names(), kwargs)

	def post(self, request, *args, **kwargs):
		kwargs = self.get_context_data(**kwargs)

		if kwargs['form'].is_valid():
			if self.post_method == 'UPDATE':
				return self.post_save(
					kwargs['form'].save(commit=False), kwargs['upload_file'])
			else:
				return self.post_save(kwargs['form'].save(commit=False))
		
		return render(request, self.get_template_names(), kwargs)

	
class BasePostCreate(LoginRequiredMixin, PermissionRequiredMixin, PostProcessView):
	models = {}
	app_name = None
	form_class = None
	raise_exception = True
	permission_required = None
	post_method = 'CREATE'

	def get_template_names(self):
		app_name = self.app_name
		return [f'{app_name}/container/{app_name}_create.html']


class BasePostEdit(LoginRequiredMixin, PermissionRequiredMixin, PostProcessView):
	models = {}
	app_name = None
	form_class = None
	permission_required = None
	post_method = 'UPDATE'

	def get_template_names(self):
		app_name = self.app_name
		return [f'{app_name}/container/{app_name}_edit.html']

	def get_object(self):
		obj = get_object_or_404(
			self.models['post_model'], pk=self.kwargs['pk'])
		return obj if obj.user == self.request.user else PermissionDenied()