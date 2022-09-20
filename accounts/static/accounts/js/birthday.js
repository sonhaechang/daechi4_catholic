function birthdaySelectMaker(d1, d2, d3) {
	if(d1 == null || d2 == null || d3 == null){
		console.warn("Unkwon Area Tag");
		return;
	}

	// 초기화
	function init(first, second){
		first ? document.getElementById(d1).innerHTML = "<option value=''>연도 선택</option>" : "";
		second ? document.getElementById(d2).innerHTML = "<option value=''>월 선택</option>" : "";
		document.getElementById(d3).innerHTML = "<option value=''>일 선택</option>";
	}
	init(true, true);

	// 회원가입과 프로필 수정 페이지가 아니면 생년월일 선택 필드 disabled 처리
	if (disabled) {
		document.getElementById(d1).setAttribute('disabled', true);
		document.getElementById(d2).setAttribute('disabled', true);
		document.getElementById(d3).setAttribute('disabled', true);
	}

	// 1자리 숫자일때 왼족에 0 추가하기
	function addZeroinLeft(e) {
		if (e <= 9) {return `0${e}`;}
			return e;
	}

	// 0이 추가된 1자리 숫자일때 왼족에 0 제가
	function removeZeroinLeft(e) {
		if (e <= 9) {return `0${e}`;}
			return e;
	}

	// 날짜 선언 및 현재 년도 가져오기
	const date = new Date();
	const selYear = date.getFullYear();

	// 년도 기본 생성
	function getYears(getY) {
		const stY = Number(getY-100)
		const sel = document.getElementById('id_year');

		for (y = stY; y <= getY; y++) {
			document.getElementById(d1).innerHTML += `<option value="${y}">${y}년</option>`;
		}
	}
	getYears(selYear);

	// 월 기본 설정
	function getMonths() {
		for (m = 1; m <= 12; m++) {
			document.getElementById(d2).innerHTML += `
				<option value="${addZeroinLeft(m)}">${m}월</option>`;
		}
	}
	getMonths();

	// 년도와 월에 맞춰서 일 생성
	function getDays(y, m) {
		const lastDay = new Date(y, m, 0).getDate();
		for (d = 1; d <= lastDay; d++) {
			document.getElementById(d3).innerHTML += `
				<option value="${addZeroinLeft(d)}">${d}일</option>`;
		}
	}

	// 년도와 월 선택시 일 생성
	document.getElementById(d2).addEventListener('change', function(e) {
		init(false, false);
		const year = document.getElementById(d1).value;
		const month = this.value;
		if (!year || !month) {
			alert('년도와 월을 먼저 선택해주세요.');
			return;
		}
		getDays(year, month);
	});

	// 마지막 일 선택시 년월일 값을 birthday field value로 변경
	document.getElementById(d3).addEventListener('change', function(e) {
		const year = document.getElementById(d1).value;
		const month = document.getElementById(d2).value;
		const day= this.value;
		document.getElementById('id_birthday').value = `${year}${month}${day}`;
	})

	// 해당 값으로 select option 선택하기
	function selectOption(target, value) {
		for(var i=0; i<target.children.length; i++) {		
			if(target.children[i].value === value) {			
				target.children[i].setAttribute('selected', '')		
			}	
		}
	}

	// 저장되어진 년도 값으로 설정
	function setYear() {
		const year = birthday['year'];
		if ( year == 'None' ) { return; }
		const targetSel = document.getElementById(d1);
		selectOption(targetSel, year);
	}
	setYear();

	// 저장되어진 월 값으로 설정
	function setMonth() {
		const month = birthday['month'];
		if ( month == 'None' ) { return; }
		const targetSel = document.getElementById(d2);
		selectOption(targetSel, month);
	}
	setMonth();

	// 저장된 년, 월 기준으로 일 생성 후 저장되어진 일 값으로 설정
	function setDay() {
		const year = birthday['day'];
		const month = birthday['day'];
		const day = birthday['day'];

		if ( year == 'None' || month == 'None' || day == 'None' ) { return; }
		getDays(year, month);

		const targetSel = document.getElementById(d3);
		selectOption(targetSel, day);
	}
	setDay();
}