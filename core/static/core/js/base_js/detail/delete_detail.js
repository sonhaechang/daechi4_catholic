const deleteBtn = document.getElementById('delete-btn');
if (deleteBtn) {
	deleteBtn.addEventListener('click', e => {
		e.preventDefault();

		axios.defaults.xsrfCookieName = 'csrftoken';
		axios.defaults.xsrfHeaderName = 'X-CSRFToken';

		const url = e.currentTarget.href;

		if (confirm('정말 삭제하시겠습니까?') == true ) {
			axios.delete(url)
				.then(function (response) {
					const data = response.data;
					if (response.status == 200) {
						window.location.href = data.redirect_url;
					} else {
						alert(response.data.error);
					}
				}).catch(function (error) {
					console.log(error.response);
				})
		}
	})
}