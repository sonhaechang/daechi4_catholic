const messages = document.querySelectorAll(".messages");
messages.forEach(event => {
	event.querySelector('.colse-msg-btn').addEventListener('click', e => {
		event.classList.add('d-none');
	});
});

setTimeout(function () {
	messages.forEach(e => {
		e.classList.add('d-none');
	});
}, 6000);