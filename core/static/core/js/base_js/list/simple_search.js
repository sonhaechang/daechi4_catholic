const cardList = ['gallery', 'picture', 'flower']
document.getElementById('simple-search-form').addEventListener('submit', e => {
	e.preventDefault();
	const q = e.target.querySelector('input[name="q"]').value;
	const url = (cardList.includes(appName)) ? `?show_type=card&q=${q}` : `?show_type=list&q=${q}`;
	window.location.href = url;
});