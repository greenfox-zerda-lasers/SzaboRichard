var myDataList = ['apple', 'banana', 'cat', 'dog'];

var changeListext = document.querySelectorAll("li");
changeListext.forEach(function(elem, index){
  elem.textContent = myDataList[index];
});
