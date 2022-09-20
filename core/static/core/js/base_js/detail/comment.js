// 대댓글 입력폼 toggle 기능 함수
function repliesToggle(e) {
	e.preventDefault();

	let replies = e.currentTarget;
	replies.innerText == '답글' ? replies.innerText = '답글 닫기' : replies.innerText = '답글';

	const commentID = e.currentTarget.getAttribute('data-comment-id');
	const repliesBlock = document.getElementById(`replies-form-block-${commentID}`);
	repliesBlock.classList.toggle('show');
};

// 대댓글 전체보기/닫기 toggle 기능 함수 
function showAllReplies(e=null, comment_id=null) {
	e.preventDefault();
	const commentID = e.currentTarget.getAttribute('data-comment-id');
	const repliesBlock = document.getElementById(`replies-block-${commentID}`);
	repliesBlock.classList.toggle('show');
};

function getCommentMoreBtn() {
	return document.getElementById('commet-more-wrapper').querySelector('button');
}

function showCommentMoreBtn() {
	getCommentMoreBtn().classList.remove('d-none');
}

function hideCommentMoreBtn() {
	getCommentMoreBtn().classList.add('d-none');
}

function checkCommentMoreBtn() {
	return getCommentMoreBtn().classList.contains('d-none');
}

var nextURL = null;

// 댓글 가져오는 함수
async function getCommet() {
	axios.defaults.xsrfCookieName = 'csrftoken';
	axios.defaults.xsrfHeaderName = 'X-CSRFToken';

	const url = nextURL != null ? nextURL : commentURL;
	const commentBlock = document.getElementById('comments-block');

	try {
		const response = await axios.get(url);

		if (response.data.results.length > 0) {
			nextURL = response.data.next;

			response.data.results.forEach(data => {
				commentBlock.insertAdjacentHTML('beforeend', makeCommentEle(data));
			});

			showCommentMoreBtn();

			if (nextURL == null) { getCommentMoreBtn().disabled = true; }
		} else {
			const noComment = `
				<p class="text-center py-5">
					<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-circle-fill" viewBox="0 0 16 16">
						<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"/>
					</svg>
					등록된 댓글이 없습니다.
				</p>`;
			commentBlock.innerHTML = noComment;
		}
		
	} catch(err) {
		console.error(err);
	}
};

getCommet();

// window.onscroll = function() {
// 	// 문서의 끝에 도달했는가?
// 	const diff = document.body.scrollHeight - parseInt(window.innerHeight);
// 	let scrollPosition = window.scrollY || document.documentElement.scrollTop;

// 	if ( (nextURL) && diff <= scrollPosition ) {
// 		getCommet();
// 	}
// }

// 삭제 button html tag 생성 함수
function makeDeleteBtnEle(data, target) {
	if (data.is_mine) {
		let onclick, comment_id, replies_id;

		if (target == 'comment') {
			comment_id = `data-comment-id="${data.id}"`;
			replies_id = '';
			onclick = 'onclick="deleteComment(event);"';
		} else {
			comment_id = `data-comment-id="${data.parent_id}"`;
			replies_id = `data-replies-id="${data.id}`;
			onclick = 'onclick="deleteComment(event);"';
		}

		return `
			<a href="#"
				class="delete-btn text-danger"
				${comment_id}
				${replies_id}
				${onclick}>
				삭제
			</a>`;
	}
	return ``
};

// 대댓글 button html tag 생성 함수
function makeRepliesBtnEle(data) {
	if (data.is_authenticated) {
		return `
			<a href="#"
				id="replies-btn-${data.id}"
				class="replies-btn ms-2"
				data-comment-id="${data.id}"
				aria-expanded="false"
				aria-controls="replies-form-block-${data.id}"
				onclick="repliesToggle(event);">
				답글
			</a>`;
	}
	return ``
};

// 대댓글 전체보기 button html tag 생성 함수
function makeRepliesAllBtnEle(data, target) {
	let ID = target == 'comment' ? data.id : data.parent_id;

	const replies = `
		<a href="#" 
			id="show-replies-all-${ID}"
			class="show-replies-all d-block pb-2" 
			aria-expanded="false"
			aria-controls="replies-form-block-${ID}"
			data-comment-id="${ID}"
			onclick="showAllReplies(event);">
			답글 전체 보기
		</a>`;
	if (target == 'comment') {
		if (data.replies.length > 0) return replies; 
		return '';
	} else {
		return replies;
	}
};

// 대댓글 입력폼 html tag 생성하는 함수
function makeRepliesFormEle(data) {
	if (data.is_authenticated) {
		return `
			<div id="replies-form-block-${data.id}" class="input-group replies-form-block">
				<textarea name="comment" cols="40" rows="1" 
					id="add-replies-${data.id}" 
					class="form-control comment" 
					placeholder="댓글 달기..." required></textarea>
					<button 
						class="btn btn-dark px-4" 
						id="button-addon2"
						type="button" 
						data-comment-id="${data.id}"
						onclick="addReplies(event);">
						댓글작성
					</button>
			</div>`;
	}
	return ``
}

// 대댓글 html tag 생성하는 함수
function makeRepliesEle(data) {
	return `
		<div id="replies-${data.id}" class="media mt-3 replies-content">
			<span class="me-3">
				<span class="rounded-circle bg-white text-muted d-inline-block text-white align-items-center justify-content-center d-flex" style="width: 30px; height: 30px; --tw-bg-opacity: 1; overflow: hidden; border: 1px solid #dbdbdb">
					<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
						<path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path>
					</svg>
				</span>
			</span>
			<div class="media-body">
				<div class="d-flex justify-content-between">
					<div>
						<h5 class="mt-0 d-inline-block me-2">
							${data.last_name}${data.first_name}
						</h5>
						<span class="text-muted created-date">
							${data.created_at}
						</span>
					</div>
					<a href="#"
						class="text-danger delete-btn"
						data-comment-id="${data.parent_id}"
						data-replies-id="${data.id}"
						onclick="deleteReplies(event);">
						삭제
					</a>
				</div>
				<p>${data.comment}</p>
			</div>
		</div>`;
};

// 댓글 html tag 생성하는 함수
function makeCommentEle(data) {
	const deleteBtn = makeDeleteBtnEle(data, 'comment');
	const repliesBtn = makeRepliesBtnEle(data);
	const repliesAllBtn = makeRepliesAllBtnEle(data, 'comment');
	const repliesForm = makeRepliesFormEle(data);

	let replies = '';
	data.replies.forEach(data => {
		replies += makeRepliesEle(data);
	});

	return `
		<div id="comment-${data.id}" class="media mt-5 border-bottom comment-content">
			<span class="me-3">
				<span class="rounded-circle bg-white text-muted d-inline-block text-white align-items-center justify-content-center d-flex" style="width: 30px; height: 30px; --tw-bg-opacity: 1; overflow: hidden; border: 1px solid #dbdbdb">
					<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
						<path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"></path>
					</svg>
				</span>
			</span>
			<div class="media-body">
				<div class="d-flex justify-content-between">
					<div>
						<h5 class="mt-0 d-inline-block me-2">
							${data.last_name}${data.first_name}
						</h5>
						<span class="text-muted created-date">
							${data.created_at}
						</span>
					</div>
					<div class="d-flex justify-content-between">
						<div class="delete-btn-block">
							${deleteBtn}
						</div>
						<div class="replies-btn-block">
							${repliesBtn}
						</div>
					</div>
				</div>
		
				<p>${data.comment}</p>

				${repliesForm}

				<div id="show-replies-all-${data.id}-block"
					class="show-replies-all-block">
					${repliesAllBtn}
				</div>

				<div id="replies-block-${data.id}" class="replies-block">
					${replies}
				</div>
			</div>
		</div>`;
};

// 댓글 등록하는 함수
function addComment(e) {
	e.preventDefault();

	axios.defaults.xsrfCookieName = 'csrftoken';
	axios.defaults.xsrfHeaderName = 'X-CSRFToken';

	// const commentURL = '{{ comment_url }}';
	let comment = document.getElementById('add-comment');

	axios.post(commentURL, {comment: comment.value,})
		.then(function (response) {
			const commentBlock = document.getElementById('comments-block');
			const comments = document.querySelectorAll('.comment-content');

			if ( comments.length == 0 ) {
				commentBlock.querySelector('p').remove();
			}

			commentBlock.insertAdjacentHTML('afterbegin', makeCommentEle(response.data));
			comment.value = '';

			if (checkCommentMoreBtn()) { showCommentMoreBtn(); }
		})
		.catch(function (err) {
			console.error(err);
		})
};

// 대댓글 등록하는 함수
function addReplies(e) {
	e.preventDefault();
	axios.defaults.xsrfCookieName = 'csrftoken';
	axios.defaults.xsrfHeaderName = 'X-CSRFToken';

	const parent_id = e.currentTarget.getAttribute('data-comment-id')
	// const commentURL = '{{ comment_url }}';
	let replies = document.getElementById(`add-replies-${parent_id}`)

	axios.post(commentURL, {
		comment: replies.value,
		parent_id: parent_id,
	})
		.then(function (response) {
			const repliesBlock = document.getElementById(`replies-block-${parent_id}`);
			const repliesContents = repliesBlock.querySelectorAll('.replies-content');
			const showRepliesAllBlock = document.getElementById(`show-replies-all-${parent_id}-block`);

			repliesBlock.insertAdjacentHTML('afterbegin', makeRepliesEle(response.data));
			repliesBlock.classList.toggle('show');

			if ( repliesContents.length == 0 ) {
				showRepliesAllBlock.insertAdjacentHTML('afterbegin', makeRepliesAllBtnEle(response.data, 'replies'));
				showRepliesAllBlock.querySelector('a').classList.add('show');
			}

			replies.value = '';
		})
		.catch(function (err) {
			console.error(err);
		})

};

// 댓글 삭제하는 함수
function deleteComment(e) {
	e.preventDefault();
	axios.defaults.xsrfCookieName = 'csrftoken';
	axios.defaults.xsrfHeaderName = 'X-CSRFToken';

	const comment_id = e.currentTarget.getAttribute('data-comment-id')
	// const commentURL = '{{ comment_url }}';
	
	if (confirm("정말 삭제하시겠습니다?")) {
		axios.delete(commentURL, {data: {'comment_id': comment_id,}})
			.then(function (response) {
				document.getElementById(`comment-${comment_id}`).remove();
				const comment = document.querySelectorAll('.comment-content');

				if ( comment.length == 0 ) {
					const noComment = `
						<p class="text-center text-muted py-5">
							<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-circle-fill" viewBox="0 0 16 16">
								<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8 4a.905.905 0 0 0-.9.995l.35 3.507a.552.552 0 0 0 1.1 0l.35-3.507A.905.905 0 0 0 8 4zm.002 6a1 1 0 1 0 0 2 1 1 0 0 0 0-2z"/>
							</svg>
							등록된 댓글이 없습니다.
						</p>`;

					document.getElementById('comments-block').innerHTML = noComment;

					if (!checkCommentMoreBtn()) { hideCommentMoreBtn(); }
				}
			}).catch(function (err) {
				console.error(err);
			})
	}
};

// 대댓글 삭제하는 함수
function deleteReplies(e) {
	e.preventDefault();
	axios.defaults.xsrfCookieName = 'csrftoken';
	axios.defaults.xsrfHeaderName = 'X-CSRFToken';

	const replies_id = e.currentTarget.getAttribute('data-replies-id')
	const comment_id = e.currentTarget.getAttribute('data-comment-id')
	// const commentURL = '{{ comment_url }}';

	if (confirm("정말 삭제하시겠습니다?")) {
		axios.delete(commentURL, {data: {'comment_id': replies_id,}})
			.then(function (response) {
				document.getElementById(`replies-${replies_id}`).remove();
				const repliesBlock = document.getElementById(`replies-block-${comment_id}`);
				const replies = repliesBlock.querySelectorAll('.replies-content');

				if ( replies.length == 0 ) {
					document.getElementById(`show-replies-all-${comment_id}`).remove();
				}
			}).catch(function (err) {
				console.error(err);
			})
	}
};
