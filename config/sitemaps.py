from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'weekly'

    def items(self):
        return ['info:church_introduce', 'info:mass_time', 'weekly:weekly_list', 
            'gallery:gallery_list', 'flower:flower_list', 'info:location']

    def location(self, item):
        return reverse(item)