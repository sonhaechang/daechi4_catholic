from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def base_pagination(**kwargs):
	''' 
	가장 기본적인 pagination 기능의 함수 댓글에 페이징 처리 또는 
	default_pagination 함수에서 사용
	'''

	request = kwargs['request']
	paginator = kwargs['paginator']
	page = request.GET.get('page', 1)

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	return queryset

def default_pagination(request, queryset, paginate_by):
	'''
	base_pagination function 기능에 추가적으로 시작 페이지와 마지막 페이지 번호를 계산하여 반환
	'''

	paginator = Paginator(queryset, paginate_by)    
	queryset = base_pagination(request=request, paginator=paginator)
	index = queryset.number -1
	max_index = len(paginator.page_range)
	start_index = index - 2 if index >= 2 else 0

	if index < 2 :
		end_index = 5 - start_index
	else :
		end_index = index + 3 if index <= max_index - 3 else max_index

	page_range = list(paginator.page_range[start_index:end_index])

	context = {
		'obj_list': queryset,
		'page_range': page_range,
		'max_index': max_index - 2	
	}

	return context