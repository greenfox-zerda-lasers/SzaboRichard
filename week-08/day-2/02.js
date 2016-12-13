// create a function that starts a setTimeout with a 3 second delay.
// - create a button with an event listener that can cancel the setTimeout

function time() {
  console.log("valami");
}
var clearThat = setTimeout(time, 10000);
var clear = clearTimeout(clearThat);

var button = document.createElement('button');
document.querySelector('button');
document.body.appendChild(button);
button.addEventListener('click', clear);
