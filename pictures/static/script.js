"use strict";

document.getElementById("parent").addEventListener("click",function(e) {
    if(e.target && e.target.id) {
        document.getElementById(String(e.target.id)).getElementsByClassName("w3-container")[0].style.visibility = "visible";
    }
});

