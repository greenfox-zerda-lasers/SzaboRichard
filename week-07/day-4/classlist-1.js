//1
var pList = document.querySelectorAll("p");

pList.forEach(function(elem){
  console.log(elem.textContent);
  if (elem.classList.contains("cat")) {
    window.alert('YEAH CAT!!');
  }
  else if (elem.textContent === "dolphin" ) {
    elem.textContent = "pear";
  }
  else if (elem.classList.contains("apple")) {
      document.querySelector(".cat").textContent =  "dog";
      document.querySelector(".apple").style.color = "red";
  };
  document.querySelector(".balloon").style.backgroundColor = "violet";
  document.querySelector(".balloon").style.borderRadius = "30%";
});

// var myThirdP = document.querySelector("cat")  window.alert('YEAH CAT!!')? : console.log("no CAT");
