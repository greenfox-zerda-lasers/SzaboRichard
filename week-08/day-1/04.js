'use strict';
// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake

function Aircraft(aircaftType, ammo) {
  this.aircaftType = aircaftType;
  switch (this.aircaftType) {
    case 'F16':
      this.ammo = (this.ammo <= 8) ? ammo :8;
      break;
    case 'F35':
      this.ammo = (this.ammo <= 12) ? ammo : 12;
      break;

  }
  }

Aircraft.prototype.baseDmg = function() {
  let returnedDmg = (this.aircraftType === 'F16') ? 30 : 50;
  return returnedDmg;
}

Aircraft.prototype.aircraftData = function() {
  return ('Type: '+ this.aircaftType +' Ammo: ' + this.ammo +' Base Damage: ' + this.baseDmg() + ' All Damage: ' +this.allDmg());
}

Aircraft.prototype.allDmg = function() {
  return this.ammo*this.baseDmg();
}

Aircraft.prototype.fight = function() {
  let rAllDmg = this.ammo*this.baseDmg();
  this.ammo = 0;
  return rAllDmg;
}

Aircraft.prototype.refill = function(ammmoAmount) {
  let maxAmmo = (this.aircraftType === 'F16') ? 8 : 12;
  let returnedAmmo = 0;
  while (this.ammo < maxAmmo) {
    this.ammo++;
    returnedAmmo++;
  }
  return returnedAmmo;
}

function Carrier(ammo) {
  this.ammo = ammo;
  this.hangarBay = []
  this.healthPoint = 3000;
  this.totalDmg = 0;
}

Carrier.prototype.statusReport = function() {
  let dataStatus = this.hangarBay.reduce(function(base, aircraft) {
    return base += aircraft.aircraftData()+"\n";
    // console.log(aircraft.aircraftData());
  }, '')
  return "Aircraft count: "+ this.hangarBay.length+", "+"Total Damage: "+this.totalDmg+", "+"Health Remaining: "+this.healthPoint+"\n"+"Aircrafts:"+"\n"+dataStatus;
 }

Carrier.prototype.addAircraft = function(plane) {
  if (plane instanceof Aircraft) {
    this.hangarBay.push(plane);
    }
}

Carrier.prototype.fill = function() {
  this.hangarBay.forEach(function(aircraft) {
      this.ammo -= aircraft.refill(this.ammo);
  }, this)
}

Carrier.prototype.fight = function() {
 this.hangarBay.forEach(function(aircraft){
   this.totalDmg += aircraft.fight();
 }, this)
 return this.totalDmg;
}

var plane = new Aircraft('F35', 0);
var plane2 = new Aircraft('F16', 0);
console.log(plane.aircraftData());
console.log(plane.fight());
console.log(plane.ammo);
var carrier = new Carrier(1000);
carrier.addAircraft(plane);
carrier.addAircraft(plane2);
carrier.fill();
console.log(carrier.ammo);
console.log(carrier.statusReport());
console.log(carrier.fight());
