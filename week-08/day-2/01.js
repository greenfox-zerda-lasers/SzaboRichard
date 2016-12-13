// create a function that when called alerts "I'm delayed" after 1 second
function alertDelay() {
  window.alert("I'm delayed");
}

setTimeout(alertDelay, 3000);
