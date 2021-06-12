let all = document.getElementById("All")
let ml = document.getElementById("ML");
let genomics = document.getElementById("Genomics");
let others = document.getElementById("Others");

let buttons = document.getElementsByClassName("btn");

const eventAll = (btn) => {
    removeActive();
    all.classList.remove("hide")
    ml.classList.add("hide");
    genomics.classList.add("hide");
    others.classList.add("hide");

    addActive(btn);
}
eventML = (btn) => {
    removeActive();
    all.classList.add("hide")
    genomics.classList.add("hide");
    others.classList.add("hide");

    ml.classList.remove("hide");
    addActive(btn);

}
eventGenomics = (btn) => {
    removeActive();
    all.classList.add("hide")
    ml.classList.add("hide");
    others.classList.add("hide");

    genomics.classList.remove("hide");  
    addActive(btn);
}
eventOthers = (btn) => {
    removeActive();
    all.classList.add("hide")
    ml.classList.add("hide");
    genomics.classList.add("hide");
    
    others.classList.remove("hide");
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