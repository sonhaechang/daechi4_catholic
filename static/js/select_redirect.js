const urlList = window.location.href.split('/');
const url = `/${urlList[3]}/${urlList[4]}/`;
const select = document.getElementById('select-redirect');

// 현재 url로 select option을 변경하는 함수
for (let i=0; i<select.options.length; i++) {
	if (select.options[i].value == url) {
		select.options[i].selected = true;
	}
} 

// select option 선택시 value에 해당 url로 이동하는 기능
select.addEventListener('change', e => {
	window.location.href = e.target.options[e.target.selectedIndex].value;
})