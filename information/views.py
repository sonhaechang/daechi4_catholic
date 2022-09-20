from django.shortcuts import render

from information.models import ( 
	FatherSister, Introduce, History, PastoralOrientation
)

# Create your views here.
def church_introduce(request):
	introduce = Introduce.objects.first()

	return render(request, 'information/container/church_introduce.html', {
		'app_name': 'church_introduce',
		'introduce': introduce
	})

def father_sister(request):
	father_sister_list = FatherSister.objects.all()

	return render(request, 'information/container/father_sister.html', {
		'app_name': 'father_sister',
		'father_sister_list': father_sister_list
	})

def location(request):
    return render(request, 'information/container/location.html', {
        'app_name': 'location'
    })

def mass_time(request):
    return render(request, 'information/container/mass_time.html', {
        'app_name': 'mass_time'
    })

def pastoral_counsil(request):
    return render(request, 'information/container/pastoral_counsil.html', {
        'app_name': 'pastoral_counsil'
    })

def history(request):
	history_list = History.objects.all()

	return render(request, 'information/container/history.html', {
		'app_name': 'history',
		'history_list': history_list
	})

def pastoral_orientation(request):
	pastoral_orientation = PastoralOrientation.objects.first()
	
	return render(request, 'information/container/pastoral_orientation.html', {
		'app_name': 'pastoral_orientation',
		'pastoral_orientation': pastoral_orientation
	})