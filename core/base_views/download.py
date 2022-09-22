import boto3
import mimetypes
import requests
import urllib

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.views.generic import TemplateView


class BaseFileDownload(LoginRequiredMixin, TemplateView):
	''' upload된 file을 download시 상속받아 사용할 Download View '''

	def get(self, request, *args, **kwargs):
		''' GET 요청을 처리하는 함수 '''

		file_name = self.kwargs['file_name']

		s3_bucket_name = settings.AWS_STORAGE_BUCKET_NAME
		s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
			aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

		bucket_location = s3.get_bucket_location(Bucket=s3_bucket_name)
		location_constraint = bucket_location['LocationConstraint']

		key_name = 'media/upload-file/' + file_name
		file_path = f'https://s3-{location_constraint}.amazonaws.com/{s3_bucket_name}/{key_name}'

		# url로 주어진 파일명, 경로 또는 URL에 기반한 파일의 유형을 추측
		file_mimetype = mimetypes.guess_type(file_path)

		# 생성된 file_path로 requests get 요청 
		f = requests.get(file_path)

		response = HttpResponse(f, content_type=file_mimetype)
		response['X-Sendfile'] = file_path

		# Content-Disposition는 HTTP Response Body에 오는 content의 기질, 성향을 알려주는 속석
		# attachment와 filename 함께 줘서 Body에 오는 값을 다운로드
		response['Content-Disposition'] = f"attachment; filename*=UTF-8\'\'{smart_str(urllib.parse.quote(file_name.encode('utf-8')))}"
		return response