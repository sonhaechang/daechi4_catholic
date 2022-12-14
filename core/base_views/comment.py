from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response

from core.paginations import DefaultPagination


class BaseCommentAPIView(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericAPIView):
	''' comment 조회, 생성, 삭제하는 모든 CommentView에서 상속 받아서 사용할 Base APIView '''

	pagination_class = DefaultPagination
	serializer_class = None
	post_model = None
	comment_model = None
	app_name = None

	def get_queryset(self):
		''' 조건에 맞는 queryset을 반환 '''

		pk = self.kwargs['post_pk']
		return self.comment_model.objects.filter(
			post__pk=pk, parent__isnull=True).order_by('-id')

	def get_post(self):
		''' pk로 queryset을 filtering 후 post object을 반환 '''

		pk = self.kwargs['post_pk']

		if self.app_name == 'school':
			school_class = self.kwargs['school_class']
			return get_object_or_404(
				self.post_model, school_class__name=school_class, pk=pk)
		return get_object_or_404(self.post_model, pk=pk)
		
	def get_serializer_class(self):
		''' serializer_class를 반환 '''

		serializer = super().get_serializer_class()
		serializer.user = self.request.user
		return serializer

	def get(self, request, *args, **kwargs):
		''' GET 요청을 처리하는 함수 '''

		serializer = self.list(request, *args, **kwargs)
		return  serializer

	def post(self, request, *args, **kwargs):
		''' POST 요청을 처리하는 함수 '''

		data = dict(request.data)
		
		parent_pk = data.get('parent_id')

		# TODO: get_or_none으로 수정 필요
		parent_obj = self.comment_model.objects.get(pk=parent_pk) if parent_pk else None

		serializer = self.get_serializer(data=data)
		serializer.is_valid(raise_exception=True)
		instance = serializer.save(
			user=request.user, 
			post=self.get_post())
		instance.parent = parent_obj
		instance.save()
		
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

	def delete(self, request, *args, **kwargs):
		''' DELETE 요청을 처리하는 함수 '''

		comment_pk = request.data.get('comment_id')

		# TODO: get_or_none으로 수정 필요
		comment = self.comment_model.objects.get(pk=comment_pk)

		if comment is None:
			return Response(status=status.HTTP_404_NOT_FOUND)

		if comment.user != self.request.user:
			return Response(status=status.HTTP_403_FORBIDDEN)

		comment.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)