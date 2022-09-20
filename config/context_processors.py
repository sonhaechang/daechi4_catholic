from django.conf import settings

from core.forms import SearchForm
from core.services import get_menu_url

from information.models import Carousel, JumbotronImage


def carousel(request):
    return {'carousel_list': Carousel.objects.all()}

def church(request):
    return {'settings': settings}

def jumbotron_image(request):
    return {'jumbotron_images': JumbotronImage.objects.all()}  

def menu_url(request):
    category_list = ['introduce', 'group', 'notice', 'participate', 'catholic']
    return {'menu_urls': [get_menu_url(category) for category in category_list]}

def search_form(request):
    return {'search_form': SearchForm()}  