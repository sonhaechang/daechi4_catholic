import django_filters

from django.db.models import Q
from django.db.models import Value as V
from django.db.models.functions import Concat

from flower.models import Flower
from freeboard.models import Freeboard
from gallery.models import Gallery
from group.models import Group
from notice.models import Notice
from picture.models import Picture
from QnA.models import QnA
from video.models import Video
from weekly.models import Weekly


class BaseFiter(django_filters.FilterSet):
	q = django_filters.CharFilter(method='q_filter')

	class Meta:
		fields = ['q']

	def q_filter(self, queryset, name, value):
		return queryset.annotate(full_name=Concat('user__last_name', V(''), 'user__first_name')).filter(
			Q(title__icontains=value) |
			Q(content__icontains=value) |
			Q(full_name__icontains=value) | 
			Q(user__first_name__icontains=value) | 
			Q(user__last_name__icontains=value)
		).distinct()


class FlowerFilter(BaseFiter):
	class Meta(BaseFiter.Meta):
		model = Flower


class FreeboardFilter(BaseFiter):
	class Meta(BaseFiter.Meta):
		model = Freeboard


class GalleryFilter(BaseFiter):
	class Meta(BaseFiter.Meta):
		model = Gallery


class GroupFilter(BaseFiter):
	class Meta(BaseFiter.Meta):
		model = Group


class NoticeFilter(BaseFiter):
	class Meta(BaseFiter.Meta):
		model = Notice

class PictureFilter(BaseFiter):
	class Meta(BaseFiter.Meta):
		model = Picture


class QnAFilter(BaseFiter):
	class Meta(BaseFiter.Meta):
		model = QnA


class VideoFilter(BaseFiter):
	class Meta(BaseFiter.Meta):
		model = Video


class WeeklyFilter(BaseFiter):
	class Meta(BaseFiter.Meta):
		model = Weekly