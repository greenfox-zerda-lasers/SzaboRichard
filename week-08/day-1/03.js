'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)
function Rocket(consumption) {
  this.consumption = consumption;
  this.fuelTank = 0;
  this.launches = 0;
}

Rocket.prototype.fill = function(amount) {
  this.fuelTank += amount;
}

Rocket.prototype.launch = function() {
  if ( this.consumption < this.fuelTank ) {
    this.fuelTank -= this.consumption;
    this.launches++;
  }
  else {
    return ('More fuel m8!!');
  }
}

var myRocket = new Rocket(4);
myRocket.fill(10);
myRocket.launch();
console.log(myRocket.launches);
