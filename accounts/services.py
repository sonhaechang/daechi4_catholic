from calendar import month
from accounts.models import Profile

def profile_create(user, data):
	Profile.objects.create(
		user = user,
		baptism = data['baptism'],
		phone_number = f'{data["phone1"]}{data["phone2"]}{data["phone3"]}',
		birthday = data['birthday'])

def profile_save(user, data):
	user.last_name = data['last_name']
	user.first_name = data['first_name']
	user.email = data['email']
	user.save()
	
	if hasattr(user, 'profile'):
		profile = user.profile
		profile = user.profile
		profile.baptism = data['baptism']
		profile.phone_number = \
			f'{data["phone1"]}{data["phone2"]}{data["phone3"]}'
		profile.birthday = data['birthday']
		profile.save()
	else:
		profile_create(user, data)

def profile_form_initial(request):
	base_initial_dict = {
		'username': request.user.username, 'last_name': request.user.last_name, 
		'first_name': request.user.first_name, 'email': request.user.email,
	}
	
	if hasattr(request.user, 'profile'):
		
		profile = request.user.profile
		base_initial_dict.update({
			'baptism': profile.baptism, 
			'birthday': profile.birthday,
			'phone1': profile.phone_number[:3],
			'phone2': profile.phone_number[3:7],
			'phone3': profile.phone_number[7:]
		})

	return base_initial_dict

def get_birthday(user):
	if hasattr(user, 'profile'):
		return user.profile.birthday