var fav_btn = document.getElementsByClassName("favourite-btn");
var i;

for (i = 0; i < fav_btn.length; i++) {
  fav_btn[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var info_panel = this.nextElementSibling;
    if (info_panel.style.maxHeight){
      info_panel.style.maxHeight = null;
    } else {
      info_panel.style.maxHeight = info_panel.scrollHeight + "px";
    }
  });
}
