const moveTopBtn = document.getElementById('move-top-btn');

// 스무스하게 맨위로 보내는 함수
moveTopBtn.addEventListener('click', e => {
	window.scrollTo({top: 0, behavior: 'smooth'});
});

// 스크롤이 특정 위치에 도달시 moveTopBtn 보여지게하는 함수
window.addEventListener('scroll', e => {
	const scrollPosition = window.scrollY || e.scrollTop;

	if (scrollPosition > 100) {
		moveTopBtn.style.display = 'flex';
	} else {
		moveTopBtn.style.display = 'none';
	}
});