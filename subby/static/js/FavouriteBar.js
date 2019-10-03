/* Opening functions for favourite menu bar */
function open_fav_menu() {
	document.getElementById("favourite-menu-button").style.visibility = "hidden";
    document.getElementById("favNav").style.width = "25%";
    document.getElementById("main-page").style.marginLeft = "25%";
}

/* Closeing functions for favourite menu bar */
function cancel_fav_menu() {
	document.getElementById("favourite-menu-button").style.visibility = "visible";
    document.getElementById("favNav").style.width = "0";
    document.getElementById("main-page").style.marginLeft = "0";
}