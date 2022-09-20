
function check_touch_device_in_businessLink() {
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
		const imgBlock = document.querySelectorAll('.img-block');
		imgBlock.forEach(ele => {
			const linkBtn = ele.querySelector('.link-btn');
			linkBtn.classList.add('d-none');

			ele.addEventListener('click', e => {
				linkBtn.click();
			});
		});
	}
}

