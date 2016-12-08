var replaceAllText = document.querySelector("p.dog");
// console.log(replaceAllText);
var iterData = document.querySelectorAll("p");

iterData.forEach(function (value) {
  value.textContent = replaceAllText.textContent;
});
