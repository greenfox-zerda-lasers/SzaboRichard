var timesData;
let dataView = document.querySelector('.data-input');
var button = document.querySelector('button');

var counter = 0;
window.addEventListener("load", function(){
  let xhr =new XMLHttpRequest();
  var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=ecf5a7de7cc04cb2b96621ac0933ae26&q=apollo+11+moon";
  xhr.open('GET', url, true);
  xhr.send();
  xhr.onreadystatechange = function() {
    if(xhr.readyState === XMLHttpRequest.DONE) {
      console.log(JSON.parse(xhr.response).response.docs);
      init(JSON.parse(xhr.response).response.docs);
    }
  }
});

function init(nyData) {
  timesData = nyData;
  return timesData;
}

button.addEventListener('click', function(e){
  if(counter >= timesData.length  ) {
    counter = 0;
  }
  counter++;
  addNewArticle(counter);
});

function addNewArticle(index) {
  let h = dataView.querySelector('h2');
  let p = dataView.querySelector('p');
  let p2 = dataView.querySelector('.date');
  let a = dataView.querySelector('a')
  h.textContent = timesData[index].lead_paragraph;
  p.textContent = timesData[index].snippet;
  p2.textContent = timesData[index].pub_date;
  a.setAttribute('href', timesData[index].web_url);
}

// timesData.forEach(function(value){
//   // p.textContent = value.response.docs
// })
