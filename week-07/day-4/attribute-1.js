//1
var myIMG = document.querySelector("img");
console.log(myIMG);
//2
myIMG.setAttribute("src",  "http://www.clixlogix.com/wp-content/uploads/2015/11/js-men.png");
//3
var grabMyA = document.querySelector("a");
grabMyA.setAttribute("href", "http://www.greenfoxacademy.com");
grabMyA.setAttribute("target", "_blank");
//4
var disableSecondButt = document.querySelector(".this-one");
disableSecondButt.setAttribute("disabled", "disabled");
//5
disableSecondButt.textContent = "Don't click me!..";
