'use strict';

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements
function logThis() {
   console.log("Mwuhaha I'm running");
}


function arrayLengthCaller(inputArray, inputFunct) {
  for (var i = 0, l = inputArray.length; i< l; i++) {
    inputFunct();
  }
}

var runner = [1,2,3]
arrayLengthCaller(runner, logThis);
