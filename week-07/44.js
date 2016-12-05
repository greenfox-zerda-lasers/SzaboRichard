'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

function minSelection (dataList) {
  var newMinReturned = 0
  for (var i = 0; i < dataList.length; i++) {
    var min = i
    for (var j = i+1; j < dataList.length; j++) {
      if( dataList[j] < dataList[min]) {
        min = j
        newMinReturned = dataList[min]
      }
    }
  }
  return newMinReturned
}

console.log(minSelection(numbers));
