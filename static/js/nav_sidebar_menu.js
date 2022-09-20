(function navSidebarMenuToggle() {
	const main = document.getElementById("main");
	const navSidebarMenu = document.getElementById("nav-sidebar-menu");

	document.getElementById('nav-sidebar-menu-open-btn').addEventListener('click', e => {
		e.preventDefault();
		navSidebarMenu.style.width = "65%";
		navSidebarMenu.classList.add('p-3');
		main.classList.add('disabled');
	});

	document.getElementById('nav-sidebar-menu-close-btn').addEventListener('click', e => {
		e.preventDefault();
		navSidebarMenu.style.width = "0";
		navSidebarMenu.classList.remove('p-3');
		main.classList.remove('disabled');
	});
})();	