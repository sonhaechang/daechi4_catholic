
const forms = document.querySelectorAll('.post_search');
forms.forEach(event => {
	event.addEventListener('submit', e => {
		e.preventDefault();
		const url = e.target.action;
		const q = e.target.querySelector('input[name="q"]').value;
		window.location.href = `${url}?show_type=list&q=${q}`;
	});
});