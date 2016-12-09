// window.alert("Test");
var container = document.querySelector('.image-container');
var prev = container.querySelector('.button-prev');
var next = container.querySelector('.button-next');
var box = container.querySelector('.show-image');
var index = 0;
// var items = ["sw.jpg", "sw1.jpg", "sw2.jpg", "sw3.jpg", "sw4.jpg"];
var wrapperThumbnails = document.querySelector('.image-container-bottom');
var imageData = [
  {
    title: 'Star Wars',
    content: 'This will be a day long remembered. It has seen the end of Kenobi, and will soon see the end of the rebellion.',
    local: "sw.jpg"
  },
  {
    title: 'Troopers',
    content: 'Whales and Rabbits',
    local: "sw1.jpg"
  },
  {
    title: 'Suprise',
    content: 'Aren’t you a little short for a stormtrooper?',
    local: "sw2.jpg"
  },
  {
    title: 'Nice title',
    content: 'I find your lack of faith disturbing.',
    local: "sw3.jpg"
  },
  {
    title: 'Where is my exam?',
    content: 'The Force is strong with this one.',
    local: "sw4.jpg"
  }];
  // var imgNum = imageData.length
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
  hTag.textContent = imageData[index].title;
  pTag.textContent = imageData[index].content;
  box.style.backgroundImage = "url(img/"+imageData[index].local+")";
};


function generetaThumb(imageData) {
  for (var i = 0; i < imageData.length; i++) {
    // var pos =
    var myThumbs = document.createElement('img');
    myThumbs.className = 'thumbs';
    myThumbs.style.backgroundImage = "url(img/"+imageData[i].local+")";
    var wraper = document.createElement('div');
    wraper.dataset.index = i;
    wraper.className = 'mini-photo-container';
    wraper.appendChild(myThumbs);
    wrapperThumbnails.appendChild(wraper);
    wraper.addEventListener('click', function(e) {
      showImg(this.dataset.index);
      // console.log(wraper);
    });
  };
};

// document.addEventListener('keypress', function(event){
//   showImg(index);
// });

generetaThumb(imageData);
