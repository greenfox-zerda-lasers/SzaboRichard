// set up a setInterval loop with 1.5 second delays
// - log the mouse coordinates on each call

var t = setInterval(logMouseMovement,1500);
var coordinates;

document.onmousemove = function(coord) {
  coordinates = coord.pageX + ', ' + coord.pageY;
}

function logMouseMovement() {
  console.log(coordinates);
}
