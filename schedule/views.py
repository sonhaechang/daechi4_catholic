from django.shortcuts import render
from django.urls import reverse

from rest_framework.generics import ListAPIView

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer

# Create your views here.
def schedule(request):
    app_name = 'schedule'
    schedule_api_url = reverse('schedule:schedule_api')

    return render(request, 'schedule/container/schedule.html', {
        'app_name': app_name,
        'schedule_api_url': schedule_api_url
    })


class SchedulAPIView(ListAPIView):
    """ 단말기 활동 분석 달력 정보 APIView  """

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def filter_queryset(self, queryset):
        year = self.request.query_params.get('year')
        month = self.request.query_params.get('month')
        queryset_filter = queryset.filter(
            start__year=year, start__month=month).order_by('-id')
        return queryset_filter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset_filter = self.filter_queryset(queryset)
        return queryset_filter