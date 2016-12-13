// Create a "tour" function that takes two functions as parameters:
//  - walk and distance
//  - distance should return an array of false values [false,false,false] with the length of a given parameter
//  - walk should go through the returned array of distance and change it to true
// //  - tour should return the result of walk
//
// function distance(param) {
//   let returnedArray = [];
//   for (var i = 0; i < param.length; i++) {
//     returnedArray.push(false);
//     // console.log(returnedArray);
//   }
//   return returnedArray;
// }
//
// function walk(dist) {
//   for (var i = 0; i < dist().length; i++) {
//     dist[i] = true;
//   }
//   // console.log(distance);
//   return dist;
// }
//
// function tour(walk, dist) {
//   return walk(distance(3));
// }
//
// console.log(tour(walk(), distance()));

function tour (walk, distance) {
  return distance(8).map(walk);
}

function distance (dist) {
  var falseArray = [];
  for (var i = 0; i < dist; i++) {
    falseArray.push(false);
  }
  return falseArray;
}

function walk () {
  return true;
}

console.log(tour(walk, distance));
