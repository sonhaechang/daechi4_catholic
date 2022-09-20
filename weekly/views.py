from core.base_views import BasePostList

from weekly.models import Weekly
from weekly.apps import WeeklyConfig


# Create your views here.
app_name = WeeklyConfig.name

class WeeklyListView(BasePostList):
    model = Weekly
    app_name = app_name
    paginate_by = 20