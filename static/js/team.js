let all = document.getElementById("All")
let Btech = document.getElementById("Btech");
let Mtech = document.getElementById("Mtech");
let PHD = document.getElementById("PHD");
let Other = document.getElementById("Other");

let buttons = document.getElementsByClassName("btn");

const eventAll = (btn) => {
    removeActive();
    all.classList.remove("hide")
    Btech.classList.add("hide");
    Mtech.classList.add("hide");
    PHD.classList.add("hide");
    Other.classList.add("hide");

    addActive(btn);
}
eventBtech = (btn) => {
    removeActive();
    all.classList.add("hide")
    Mtech.classList.add("hide");
    PHD.classList.add("hide");
    Other.classList.add("hide");

    Btech.classList.remove("hide");
    addActive(btn);

}
eventMtech = (btn) => {
    removeActive();
    all.classList.add("hide")
    Btech.classList.add("hide");
    PHD.classList.add("hide");
    Other.classList.add("hide");

    Mtech.classList.remove("hide");  
    addActive(btn);
}
eventPHD = (btn) => {
    removeActive();
    all.classList.add("hide")
    Btech.classList.add("hide");
    Mtech.classList.add("hide");
    Other.classList.add("hide");

    PHD.classList.remove("hide");
    addActive(btn);
}

eventOther = (btn) => {
    removeActive();
    all.classList.add("hide")
    Btech.classList.add("hide");
    Mtech.classList.add("hide");
    PHD.classList.add("hide");
    
    Other.classList.remove("hide");
    addActive(btn);
}

const removeActive = () => {
    for(let i = 0; i < buttons.length; i++){
        buttons[i].classList.remove("active");
    }
}

function addActive(btn){
    btn.classList.add("active")
}