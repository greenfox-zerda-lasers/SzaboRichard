//1
var asteroidList = document.querySelector('.asteroids');

var newAsteroid = document.createElement('li');
newAsteroid.id = 'first-adding';
newAsteroid.textContent = 'The Green Fox';
asteroidList.appendChild(newAsteroid);

var lampLighter = document.createElement('li');
lampLighter.textContent = ' The Lamplighter';
asteroidList.appendChild(lampLighter);

var myNewHeading = document.createElement('h1');
myNewHeading.textContent = 'I can add elements to the DOM';
document.querySelector('.container').appendChild(myNewHeading);
myNewHeading.style.color = "green";

var newATag = document.createElement('a');
newATag.setAttribute("href", "http://www.greenfoxacademy.com/");
var foxIMG = document.createElement('img');
foxIMG.setAttribute("src", "https://slm-assets1.secondlife.com/assets/1548684/lightbox/19f94ec2b81c379892b84401c01a6993.jpg?1277247668");
newATag.appendChild(foxIMG);
document.querySelector('.container').appendChild(newATag);
