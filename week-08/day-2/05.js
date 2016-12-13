// Add a click event listener to a <button> and console.log its innerHTML
var button = document.createElement('button');
document.body.appendChild(button);
button.innerHTML = "kjfasfjadbjfjdjsfj";
button.addEventListener('click', logMe);
function logMe() {
  console.log(button.innerHTML);
}
