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
	def get(self, request, *args, **kwargs):
		file_name = self.kwargs['file_name']

		s3_bucket_name = settings.AWS_STORAGE_BUCKET_NAME
		s3 = boto3.client('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
			aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)

		bucket_location = s3.get_bucket_location(Bucket=s3_bucket_name)
		location_constraint = bucket_location['LocationConstraint']

		key_name = 'media/upload-file/' + file_name
		file_path = f'https://s3-{location_constraint}.amazonaws.com/{s3_bucket_name}/{key_name}'
		file_mimetype = mimetypes.guess_type(file_path)

		f = requests.get(file_path)

		response = HttpResponse(f, content_type=file_mimetype)
		response['X-Sendfile'] = file_path
		response['Content-Disposition'] = f"attachment; filename*=UTF-8\'\'{smart_str(urllib.parse.quote(file_name.encode('utf-8')))}"
		return response