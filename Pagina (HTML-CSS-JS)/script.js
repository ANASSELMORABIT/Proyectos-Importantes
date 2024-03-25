var text = ["Ciber Seguridad","¿QUÉ ES LA CIBERSEGURIDAD?", "LA IMPORTANCIA DE CIBERSEGURIDAD", "Medidas de CIBERSEGURIDAD","PRINCIPALES AMENAZAS"];

var counter = 0;
var elem = document.getElementById("changeText");
var elemContainer = document.getElementById("changeTextContainer");
var inst = setInterval(change, 1000);

function showText() {
    elemContainer.style.opacity = 1;
}

function change() {
    elemContainer.style.opacity = 0;
    elem.innerHTML = text[counter];
    setTimeout(showText, 200);
    counter++;
    if (counter >= text.length) {
        counter = 0;
    }
}
const f = document.getElementById("foo");
document.addEventListener(
  "click",
  (ev) => {
    f.style.transform = `translateY(${ev.clientY - 25}px)`;
    f.style.transform += `translateX(${ev.clientX - 25}px)`;
  },
  false,
);