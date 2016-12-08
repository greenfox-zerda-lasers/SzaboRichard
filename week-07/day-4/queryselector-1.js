//1
var king = document.getElementById('b325');
console.log(king);
//2
var conceitedMan = document.getElementsByClassName("asteroid b326");

window.alert(king+" " + conceitedMan[0]);

var businessLamp =  document.getElementsByClassName("asteroid big");
//3
console.group("3as feladat");
console.log(businessLamp[0], businessLamp[1]);
console.groupEnd();
//4
var conceitedKing = document.querySelectorAll(".container .asteroid");
console.group("4es feladat");
console.log(conceitedKing);
console.groupEnd();
for(var i = 0; i < conceitedKing.length; i++) {

  window.alert(conceitedKing[i]);
};


//5
var noBusiness =  document.querySelectorAll("div.asteroid");;
console.group("5ös feladat");
console.log(noBusiness);
console.groupEnd();
//6
var allBizniss = document.getElementsByTagName("p");
console.group("6os feladat");
console.log(allBizniss);
console.groupEnd();
window.alert(allBizniss);
