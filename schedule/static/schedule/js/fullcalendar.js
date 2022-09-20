document.addEventListener('DOMContentLoaded', () => {
	let calendarEl = document.getElementById('calendar');
	let calendar = new FullCalendar.Calendar(calendarEl, {
		initialView: 'dayGridMonth',
		themeSystem: 'bootstrap5',
		locale: 'ko',
		eventDidMount: function(info) {
			// console.log(info.event.title);
		},
	});

	calendar.render();			

	const getData = () => {
		const config = {headers: {"Content-Type": "application/json"}};
		const date = document.querySelector('.fc-toolbar-title').innerText.split(' ');
		const year = date[0].slice(0, -1);
		const month = date[1].slice(0, -1);

		axios.get(url, {params: {year: year, month: month}}, config)
			.then(function (response) {
				const data = response.data;
				if (data) {
					data.forEach(e => {
						calendar.addEvent({
							id: e.start,
							title: e.title,
							start: e.start,
							end: e.end
						});
					});
				}		
			}).catch(function (error) {
				error.response
			})
	}

	getData();

	const fcTodayBtn = document.querySelector('.fc-today-button');
	fcTodayBtn.classList.remove('btn-primary');
	fcTodayBtn.classList.add('btn-dark');

	const fcPrevBtn = document.querySelector('.fc-prev-button');
	fcPrevBtn.classList.remove('btn-primary');
	fcPrevBtn.classList.add('btn-dark');
	fcPrevBtn.addEventListener('click', e => {
		calendar.removeAllEvents();
		getData();
	});

	const fcNextBtn = document.querySelector('.fc-next-button');
	fcNextBtn.classList.remove('btn-primary');
	fcNextBtn.classList.add('btn-dark');
	fcNextBtn.addEventListener('click', e => {
		calendar.removeAllEvents();
		getData();
	});
});