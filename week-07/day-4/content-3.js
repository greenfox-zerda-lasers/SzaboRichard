var neededTextFromFirstP = document.querySelector("body p");
// console.log(neededTextFromFirstP);
//1
var output1TextModify = document.querySelector(".output1");
// console.log(output1TextModify);
output1TextModify.textContent = neededTextFromFirstP.textContent;

//2
var output2TextModify = document.querySelector(".output2");
output2TextModify.innerHTML = neededTextFromFirstP.innerHTML;
