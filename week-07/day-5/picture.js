// window.alert("Test");
var container = document.querySelector('.image-container');
var prev = container.querySelector('.button-prev');
var next = container.querySelector('.button-next');
var box = container.querySelector('.show-image');
var index = 0;
var items = ["sw.jpg", "sw1.jpg", "sw2.jpg", "sw3.jpg", "sw4.jpg"];
var amount = items.length;

next.addEventListener('click', function (e) {
  index++;
  if (index === amount) {
    index = 0;
  };
  console.log(index);
});

prev.addEventListener('click', function (e) {
  index--;
  if (index < 0) {
    index = 0;
  }
  console.log(index);
});

function showImg (index) {
  for (var i = 0; i < itmes.length; i++) {
    itmes[i]
  }

  //egy index amit lekezel a galéria képmgejelenítés,
}

function gallery(){
  // items.forEach(function(elem){
  //   // if (onclick) {
  //   //
  //   // }
  //   box.style.backgroundImage = "url(img/"+elem+")";
  //   console.log(box.setAttribute);
  // });
  //thumbnaileket begyújteni, foreach loopon belül események
};
// var datalist = ;
gallery();
