// 페이지네이션 페이지 버튼 클릭시 show type에 따라서 url 생성 후 페이지 이동
const pageLink = document.querySelectorAll('.page-link');
pageLink.forEach(event => {
	event.addEventListener('click', e => {
		e.preventDefault();
		const page = e.target.getAttribute('data-page');
		if (page) {
			const url = new URLSearchParams(location.search);
			url.set('page', page);
			location.href = `?${url.toString()}`;

			// const params = window.location.search.split('&');
			// const showType = window.location.search.split('&')[0];
			// window.location.href = `${showType}&page=${page}`;
		}
	});
});