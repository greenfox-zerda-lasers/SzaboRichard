// window.alert("Test");
var container = document.querySelector('.image-container');
var prev = container.querySelector('.button-prev');
var next = container.querySelector('.button-next');
var box = container.querySelector('.show-image');
var index = 0;
var items = ["sw.jpg", "sw1.jpg", "sw2.jpg", "sw3.jpg", "sw4.jpg"];
var imageData = [
  {
    title: 'Star Wars',
    content: 'Foxes',
    local: "sw.jpg"
  },
  {
    title: 'Troopers',
    content: 'Whales and Rabbits',
    local: "sw1.jpg"
  },
  {
    title: 'Suprise',
    content: 'Baobabs and Roses',
    local: "sw2.jpg"
  },
  {
    title: 'StW',
    content: 'Giant monsters',
    local: "sw3.jpg"
  },
  {
    title: 'Where is my exam?',
    content: 'Sheep',
    local: "sw4.jpg"
  }];
var amount = items.length;

next.addEventListener('click', function (e) {
  index++;
  if (index === amount) {
    index = 0;
  };
  console.log(index);
  showImg(index);
});

prev.addEventListener('click', function (e) {
  index--;
  if (index < 0) {
    index = 0;
  }
  console.log(items[index]);
  showImg(index);
});

function showImg (index) {
  box.style.backgroundImage = "url(img/"+imageData[index].local+")";
};

function gallery(){
  // items.forEach(function(elem){
  //   // if (onclick) {
  //   //
  //   // }
  //   console.log(box.setAttribute);
  // });
  //thumbnaileket begyújteni, foreach loopon belül események
};

gallery();
