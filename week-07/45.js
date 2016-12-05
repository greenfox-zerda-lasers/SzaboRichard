'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array
function shortestStringSearcher(dataArray) {
  for (var i = 0; i < dataArray.length; i++) {
    var min = i
    for (var j = i+1; j < dataArray.length; j++) {
      if( dataArray[j].length < dataArray[min].length) {
        min = j
      }
    }
  }
  return dataArray[min]
}

console.log(shortestStringSearcher(names));
