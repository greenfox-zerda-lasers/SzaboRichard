//1
  var heading = document.querySelector("h1");
  window.alert(heading.textContent);


//2
var firstP = document.querySelector("body p");
console.group("Second task log");
console.log(firstP.textContent);
console.groupEnd();

//3
var alertSecondP = document.getElementsByClassName("other");
for (var i = 0; i < alertSecondP.length; i++){
  window.alert(alertSecondP[i].textContent);
}

//4
 heading.textContent = "New content.";

//5
var lastP = document.querySelector("p.result");
lastP.textContent = firstP.textContent;
// console.log("last", lastP.lastElementChild.textContent);
