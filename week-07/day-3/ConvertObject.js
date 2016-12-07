// Create an object that has several converter methods:
//
// float2string(num) it should convert a float number to a string, for example 12.24 -> '12.24'
// string2float(str) it should convert a string to a float number, for example '12.24' -> 12.24
// int2roman(number) it should convert an int number to a roman number as a string, for example 12 -> 'XII'
// roman2int(number) it should convert a roman number as a string to an int, for example 'XII' -> 12 please try to avoid using the built in conversion methods
function romanize(num) {
  var lookup = {M:1000,CM:900,D:500,CD:400,C:100,XC:90,L:50,XL:40,X:10,IX:9,V:5,IV:4,I:1},roman = '',i;
  for ( i in lookup ) {
    while ( num >= lookup[i] ) {
      roman += i;
      num -= lookup[i];
    }
  }
  return roman;
}

function Converter() {
  this.float2string = function(num) {
    return num +"";
  };
  this.string2float = function(string) {
    return Math.floor(string);
  };
  this.int2roman = function(number) {
    return romanize(number);
  };
}

var conv = new Converter();
console.log(conv.float2string(12.24));
console.log(conv.string2float("12.24"));
console.log(typeof(conv.string2float("12.24")));
console.log(typeof(conv.float2string(12.24)));
console.log(conv.int2roman(12));
