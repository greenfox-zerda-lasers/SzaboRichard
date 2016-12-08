// var button = document.querySelector('button');

var button = document.querySelector('button');
var partyDiv = document.querySelector('div');

 function partyNow () {
   if (partyDiv.classList.contains("party")) {
     partyDiv.classList.remove("party");
   } else {
     partyDiv.classList.add("party");
   }
 }

button.addEventListener('click', partyNow);
