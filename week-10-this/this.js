'use strict';

// function cica (neve) {
//   // this.valami = 2;
//   this.neve = neve;
//   console.log(this);
// //   // console.log('barmi');
// //   // this.nyavog = 'miau';
// // }
//
// cica.prototype.bajusz = 3;
// cica.prototype.getbajusz = function () {
//   console.log(this.bajusz);
// }
//
// //function invocation
// // cica();
// //global object nem strict modeban
// //undifiend strict modban
//
// const kanape = {
//   // allat: function cica2 () {
//   //   console.log(this);
//   // }
//   allat: cica
// }
//
// //method invocation
// kanape.allat();
// //this: kanape
//
// // constructor invocation
// var mici = new cica ('Mici');
// var feri = new cica ('Feri');
// // this a megfelelő cica() példány

// feri.getbajusz();
// mici.getbajusz();
// cica.prototype.bajusz = 10;
// feri.getbajusz();
// mici.getbajusz();


function cica (neve) {
  console.log(this);
  // console.log(neve);
}

// indirect invocation
// cica.call('hal', 'barmi');
// cica.apply('barmi', ['feri']);
//this: amit atadunk parameterkent

var mici = cica.bind('barmi');
mici();
