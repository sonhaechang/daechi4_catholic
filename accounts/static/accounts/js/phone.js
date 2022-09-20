function phoneNumber() {
	const phone2 = document.getElementById('id_phone2');
	const phone3 = document.getElementById('id_phone3');

	function inputValueSlicing(e, len) {
		if (e.length > len) {return e.slice(0, len);}
		return e;
	};

	phone2.addEventListener('input', e => {
		e.target.value = inputValueSlicing(e.target.value, 4);
	});

	phone3.addEventListener('input', e => {
		e.target.value = inputValueSlicing(e.target.value, 4);
	});
}
