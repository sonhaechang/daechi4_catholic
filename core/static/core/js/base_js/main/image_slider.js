function makeSlideShow(slidesId) {
	const slider = document.getElementById(slidesId);
	const sliderInner = slider.querySelector('.slider-inner');

	const prevBtn = slider.querySelector('.prev-btn');
	const nextBtn = slider.querySelector('.next-btn');
	const indicators = slider.querySelector('.slider-indicators-scrollbar-drag');

	const sliderContent = sliderInner.querySelectorAll('.slider-content');
	let imgWidth = sliderContent[0].clientWidth;

	let xDown = null;
	let yDown = null;
	let index = 0;
	let totalIndex;
	
	function setTotalIndex() {
		if (matchMedia("screen and (min-width: 768px)").matches) { totalIndex = 7;} 
		else { totalIndex = 8; }
	}
	setTotalIndex();
	

	window.addEventListener('resize', () => {
		imgWidth = sliderContent[0].clientWidth;
		setTotalIndex();
	});

	// 터치 가능한 기기인지 확인
	function is_touch_device() {
		try {
			document.createEvent("TouchEvent");
			return true;
		} catch (e) {
			return false;
		}
	}

	if (is_touch_device()) {
		prevBtn.classList.add('d-none');
		nextBtn.classList.add('d-none');
	}
	
	function nextImg() {
		index += 1;
		if ( index === totalIndex ) { index = 0; }
		moveHandler();
	};

	function prevImg() {
		index -= 1;
		if ( index < 0 ) { index = totalIndex - 1; }
		moveHandler();
	};

	function moveHandler(e) {
		sliderInner.style.transform = "translate3d(-"+(index * imgWidth)+"px, 0px, 0px)";
		indicators.style.transform = "translate3d("+(index * 20)+"px, 0px, 0px)";
	};

	function handleTouchStart(e) {
		xDown = e.touches[0].clientX;
		yDown = e.touches[0].clientY;
	};

	function handleTouchMove(e) {
		if ( !xDown || !yDown) { return; }

		const xUp = e.touches[0].clientX;
		const yUp = e.touches[0].clientY;

		const xDiff = xDown - xUp;
		const yDiff = yDown - yUp;

		if ( Math.abs(xDiff) > Math.abs(yDiff) ) {
			if ( xDiff>0 ) {
				if ( yDiff ) { e.preventDefault(); }
				nextImg();
			} else {
				if ( yDiff ) { e.preventDefault(); }
				prevImg();
			}
		}

		xDown = null;
		yDown = null;
	};

	prevBtn.addEventListener('click', function(e) { prevImg(); });
	nextBtn.addEventListener('click', function(e) { nextImg(); });

	slider.addEventListener('touchstart', handleTouchStart, false);
	slider.addEventListener('touchmove', handleTouchMove, false);

	setInterval(() => nextImg(), 3000);
}