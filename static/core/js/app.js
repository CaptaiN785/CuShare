var navList = document.querySelectorAll(".nav-item");
navList.forEach((x)=>{
    x.childNodes[0].className = "nav-item";
    if(x.childNodes[0].href == location.href){
        x.childNodes[0].className = "nav-item active";
    }
})

var navBtn = document.getElementById("nav-btn");
navBtn.addEventListener("click", function(){
    if(navBtn.innerText === "="){
        navBtn.className = "nav-btn btn-close";
        navBtn.innerText = "X";
        document.querySelector(".nav-list").style.display = "block";
    }else{
        navBtn.className = "nav-btn btn-open";
        document.querySelector(".nav-list").style.display = "none";
        navBtn.innerText = "=";
    }
})