
// imitate the setInterval functionality with setTimeouts (recreate the previous excersize)
var coord;
var coordinates;
document.onmousemove = function(coord) {
   coordinates = coord.pageX + ', ' + coord.pageY;
  // logMouseMovement();
}

function logMouseMovement() {
  console.log(coordinates);
  setTimeout(logMouseMovement, 1500);
}

logMouseMovement();
