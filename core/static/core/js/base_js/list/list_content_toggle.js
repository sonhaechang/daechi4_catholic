const showListBtn = document.getElementById('showListBtn');
const showCardBtn = document.getElementById('showCardBtn');
const listBlock = document.getElementById('list_block');
const cardBlock = document.getElementById('card_block');

function showBtnToggle(self, showBtnEle, showType) {
	if (self.classList.contains('btn-light')) {
		self.classList.toggle('btn-light');
		self.classList.toggle('btn-dark');
		showBtnEle.classList.toggle('btn-dark');
		showBtnEle.classList.toggle('btn-light');
		listBlock.classList.toggle('d-none');
		cardBlock.classList.toggle('d-none');
		changeUrl(showType);
	}
}

function changeUrl(showType) {
	const urlList = window.location.href.split('?');
	const url = urlList[0];
	const params = urlList[1].split('&');

	// show type에 따라 기본 url 생성 
	let fullUrl = `${url}?show_type=${showType}`

	// show_type을 제외한 url params를 반복하여 기본 url에 params 추가  
	if (urlList[1].split('&').length > 1) {
		for(i=1; i<params.length; i++) {
			fullUrl = fullUrl + `&${params[i]}`
		}
	}

	// 생성된 주소로 pushState하여 이동
	window.history.pushState(null, null, fullUrl);
}

showListBtn.addEventListener('click', e => {
	const self = e.currentTarget;
	showBtnToggle(self, showCardBtn, 'list');
});

showCardBtn.addEventListener('click', e => {
	const self = e.currentTarget;
	showBtnToggle(self, showListBtn, 'card');
});