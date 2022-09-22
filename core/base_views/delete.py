from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response


class BasePostDelete(APIView):
    ''' Post를 삭제하는 모든 DeleteView에서 상속 받아서 사용할 Base APIView '''

    model = None
    app_name = None
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        ''' pk로 queryset을 filtering 후 object을 반환 '''

        return get_object_or_404(self.model, pk=self.kwargs['pk'])

    def get_success_url(self, school_class):
        ''' form에서 유효성 검사를 통과후 rediect url을 반환 '''

        app_name = self.app_name

        if school_class is not None:
            return reverse(
                f'{app_name}:{app_name}_list', 
                kwargs={'school_class': school_class})
        else:
            return reverse(f'{app_name}:{app_name}_list')

    def delete(self, request, *args, **kwargs):
        ''' DELETE 요청을 처리하는 함수 '''

        obj = self.get_object()
        school_class = obj.school_class if self.app_name == 'school' else None
        
        if obj.user != self.request.user:
            data = {'error': _('작성자가 아니라 삭제할 수 없습니다.')}
            return Response(data=data, status=status.HTTP_403_FORBIDDEN)

        obj.delete()
        messages.success(self.request, _('포스팅을 삭제했습니다.'))
        data = {'redirect_url': self.get_success_url(school_class)}
        return Response(data=data, status=status.HTTP_200_OK)     