'use strict';
var container = document.querySelector('.image-container');
var prev = container.querySelector('.button-prev');
var next = container.querySelector('.button-next');
var box = container.querySelector('.show-image');
var index = 0;
var wrapperThumbnails = document.querySelector('.image-container-bottom');
var imageData;

window.onload = function() {
  let httpRequest = new XMLHttpRequest();
  httpRequest.open('GET', 'http://api.giphy.com/v1/gifs/search?q=star+wars+rogue+one&limit=16&api_key=dc6zaTOxFJmzC   ', true);
  httpRequest.send(null);
  httpRequest.onreadystatechange = function() {
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
      init(JSON.parse(httpRequest.response).data);
      // console.log(JSON.parse(httpRequest.response));
    }
  }};

  function init(giphyData) {
    imageData = giphyData;
    // console.log(imageData);
    generetaThumb(imageData);
    showImg(0);
    return imageData;
  }

// box.style.backgroundImage = "url(img/"+imageData+")";
next.addEventListener('click', function (e) {
  index++;
  if (index === imageData.length) {
    index = 0;
  };
  showImg(index);
});

prev.addEventListener('click', function (e) {
  index--;
  if (index < 0) {
    index = imageData.length;
  }
  showImg(index);
});

function showImg (index) {
  var hTag = document.querySelector('.show-image-content h1');
  var pTag = document.querySelector('.show-image-content p');
  // hTag.textContent = imageData[index].title;
  // pTag.textContent = imageData[index].content;
  box.style.backgroundImage = "url("+imageData[index].images.original.url+")";
};


function generetaThumb(imageData) {
  for (var i = 0; i < imageData.length; i++) {
    // var pos =
    var myThumbs = document.createElement('img');
    myThumbs.className = 'thumbs';
    myThumbs.style.backgroundImage = "url("+imageData[i].images.original_still.url+")";
    var wraper = document.createElement('div');
    wraper.dataset.index = i;
    wraper.className = 'mini-photo-container';
    wraper.appendChild(myThumbs);
    wrapperThumbnails.appendChild(wraper);
    wraper.addEventListener('click', function(e) {
      showImg(this.dataset.index);
      // showImg(dataset.index);
      // console.log(wraper);
    });
  };
};
