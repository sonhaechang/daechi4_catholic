import re
from django.urls import reverse

from django_summernote import models as summer_model


def get_menu_url(value, request=None):
	menu_urls = {
		'introduce': {
			'name': 'introduce',
			'apps': [
				{'name': 'church_introduce', 'url': reverse('information:church_introduce')}, 
				{'name': 'history', 'url': reverse('information:history')},
				{'name': 'mass_time', 'url': reverse('information:mass_time')},
				{'name': 'father_sister', 'url': reverse('information:father_sister')},
				{'name': 'location', 'url': reverse('information:location')}  
			],
		},
		'group': {
            'name': 'group',
            'apps': [
                {'name': 'pastoral_counsil', 'url': reverse('information:pastoral_counsil')},
                {'name': 'pastoral_orientation', 'url': reverse('information:pastoral_orientation')}, 
                {'name': 'group', 'url': reverse('group:group_list')},
                {'name': 'school', 'url': reverse('school:school_list', args=['초등부'])}
            ]
        },
        'notice': {
            'name': 'notice',
            'apps': [
                {'name': 'notice', 'url': reverse('notice:notice_list')}, 
                {'name': 'weekly', 'url': reverse('weekly:weekly_list')},
                {'name': 'schedule', 'url': reverse('schedule:schedule')},
                {'name': 'gallery', 'url': reverse('gallery:gallery_list')},
                {'name': 'flower', 'url': reverse('flower:flower_list')}
            ]
        },
        'participate': {
            'name': 'participate',
            'apps': [
                {'name': 'picture', 'url': reverse('picture:picture_list')}, 
                {'name': 'video', 'url': reverse('video:video_list')},
                {'name': 'QnA', 'url': reverse('QnA:QnA_list')},
                {'name': 'freeboard', 'url': reverse('freeboard:freeboard_list')}
            ]
        },
        'catholic': {
            'name': 'catholic',
            'apps': [
                {'name': 'seoul_archdiocese', 'url': 'http://aos.catholic.or.kr/'},
                {'name': 'catholic_chant', 'url':'https://maria.catholic.or.kr/sungga/search/sungga_search.asp'},
                {'name': 'daliy_mass', 'url': 'http://info.catholic.or.kr/missa/'}
            ]
        },
		'my_page': {
            'name': 'my_page',
            'apps': [
                {'name': 'profile', 'url': reverse('profile')},
                {'name': 'change_password', 'url': reverse('change_password')},
            ]
        },
		'search': {
            'name': 'search',
            'apps': [
                {'name': 'search', 'url': 'javascript:void(0);'},
            ]
        },
	}

	if request is not None:
		if request.user.is_authenticated:
			next_path = request.path
			menu_urls['my_page']['apps'].insert(3, 
				{'name': 'logout', 'url': f'{reverse("logout")}?next={next_path}'})
				
		if request.user.is_superuser:
			menu_urls['my_page']['apps'].insert(2, {'name': 'admin', 'url': '/admin'})

	return menu_urls[value]

def base_summernote_crate(instance):
	content = instance.content
	instance.thumbnail_set.all().delete()

	image = re.search(r'([0-9])\d+\-([0-9])\d+\-([0-9])\d+\/([A-Za-z0-9])\w+\-([A-Za-z0-9])\w+\-([A-Za-z0-9])\w+([A-Za-z0-9])\w+\-([A-Za-z0-9])\w+\-([A-Za-z0-9])\w+\.(?:jpg|gif|png|JPG|jpeg|ico)',
	content)

	if image:
		return f'/django-summernote/{image.group()}'
	else:
		return

def base_summernote_delete(content):
	attachments = summer_model.Attachment.objects.all()
	attachment = ['/'.join(i.file.url.split('/')[2:]) for i in attachments]

	for i in attachment:
		if content.find(i) != -1:
			attachments.filter(file=i).delete()