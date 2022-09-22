from calendar import month
from accounts.models import Profile

def profile_create(user, data):
	''' profile을 생성 (login시 사용) '''

	Profile.objects.create(
		user = user,
		baptism = data['baptism'],
		phone_number = f'{data["phone1"]}{data["phone2"]}{data["phone3"]}',
		birthday = data['birthday'])

def profile_save(user, data):
	''' profile 저장 (profile 수정시 사용) '''

	user.last_name = data['last_name']
	user.first_name = data['first_name']
	user.email = data['email']
	user.save()
	
	# user object에 profile이 있다면 수정 없다면 생성, 
	# createsuperuser로 계정 생성시 profile이 없는 경우도 있음
	if hasattr(user, 'profile'):
		profile = user.profile
		profile.baptism = data['baptism']
		profile.phone_number = \
			f'{data["phone1"]}{data["phone2"]}{data["phone3"]}'
		profile.birthday = data['birthday']
		profile.save()
	else:
		profile_create(user, data)

def profile_form_initial(request):
	''' profile form에 초기값 생성 및 반환 '''

	base_initial_dict = {
		'username': request.user.username, 'last_name': request.user.last_name, 
		'first_name': request.user.first_name, 'email': request.user.email,
	}
	
	# user object에 profile이 있다면 profile 초기값 추가
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
	''' user object에 profile이 있다면 생년월일 반환 '''

	if hasattr(user, 'profile'):
		return user.profile.birthday