document.addEventListener('DOMContentLoaded', () => {
	const agreements = document.querySelectorAll('input[type="checkbox"]:not(#agree-all)');
	const agreeAll = document.getElementById('agree-all'); 

	agreements.forEach(event => {
		event.addEventListener('click', event => {
			for(var i = 0; i < agreements.length; i++) { 
				if(!agreements[i].checked) { 
					agreeAll.checked = false; 
					return; 
				} 
			} 
			agreeAll.checked = true; 
		});
	});

	document.getElementById('agree-all').addEventListener('click', e => {
		for(var i = 0; i < agreements.length; i++) { 
			agreements[i].checked = e.currentTarget.checked; 
		} 
	});

	document.getElementById('agree-form').addEventListener('submit', e => {
		e.preventDefault();
		if (!agreeAll.checked) {
			alert('회원가입약관의 내용에 모두 동의하셔야 회원가입 하실 수 있습니다.');
			return;
		}
		e.currentTarget.submit();
	});
})