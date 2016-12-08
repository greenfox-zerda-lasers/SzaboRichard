

document.querySelector("body a").setAttribute("href", "javascript:(function bookmarkletTwo() {var imgContainer = document.querySelectorAll('img');imgContainer.forEach(function(elem) {elem.setAttribute('src', 'http://bit.ly/lpgreenfox');});})();");
