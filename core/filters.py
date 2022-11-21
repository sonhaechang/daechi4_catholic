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
	''' 
	django_filters를 사용한 filterset class 생성 
	base filter로 각 개시판 필터에서 상속 받아서 사용
	'''

	q = django_filters.CharFilter(method='q_filter')

	class Meta:
		fields = ['q']

	def q_filter(self, queryset, name, value):
		''' 풀네임(이름), 성, 이름, 제목, 내용에 검색결과가 있는지 filtering후 반환 '''

		return queryset.annotate(full_name=Concat('user__last_name', V(''), 'user__first_name')).filter(
			Q(title__icontains=value) |
			Q(content__icontains=value) |
			Q(full_name__icontains=value) | 
			Q(user__first_name__icontains=value) | 
			Q(user__last_name__icontains=value)
		).distinct()


class FlowerFilter(BaseFiter):
	''' 제대꽃 검색 필터 '''

	class Meta(BaseFiter.Meta):
		model = Flower


class FreeboardFilter(BaseFiter):
	''' 자유 게시판 검색 필터 '''

	class Meta(BaseFiter.Meta):
		model = Freeboard


class GalleryFilter(BaseFiter):
	''' 행사사진 검색 필터 '''

	class Meta(BaseFiter.Meta):
		model = Gallery


class GroupFilter(BaseFiter):
	''' 단체 게시판 검색 필터 '''

	class Meta(BaseFiter.Meta):
		model = Group


class NoticeFilter(BaseFiter):
	''' 공지사항 검색 필터 '''
	class Meta(BaseFiter.Meta):
		model = Notice

class PictureFilter(BaseFiter):
	''' 우리들 사진 검색 필터 '''

	class Meta(BaseFiter.Meta):
		model = Picture


class QnAFilter(BaseFiter):
	''' 묻고 답하기 검색 필터 '''

	class Meta(BaseFiter.Meta):
		model = QnA


class VideoFilter(BaseFiter):
	''' 우리들 영상 검색 필터 '''

	class Meta(BaseFiter.Meta):
		model = Video


class WeeklyFilter(BaseFiter):
	''' 주보 검색 필터 '''

	class Meta(BaseFiter.Meta):
		model = Weekly