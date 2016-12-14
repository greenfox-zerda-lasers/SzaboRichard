var movieData;
var dataView = document.querySelector('.data-input');
var button = document.querySelector('button');

// var counter = 0;
(function(){
  let xhr =new XMLHttpRequest();
  var url = "https://sheetsu.com/apis/v1.0/7654fbe24554";
  xhr.open('GET', url, true);
  xhr.send();
  xhr.onreadystatechange = function() {
    if(xhr.readyState === XMLHttpRequest.DONE) {
      console.log(JSON.parse(xhr.response));
      init(JSON.parse(xhr.response));
    }
  }
})();

function addThisMovie() {
  let xhr = new XMLHttpRequest();
  var url = 'https://sheetsu.com/apis/v1.0/7654fbe24554';
  xhr.open('POST', url, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(getData())
}

button.addEventListener('click', addThisMovie);

function getData() {
  var returnedMovie = {};
  returnedMovie.MovieTitle = document.querySelector('input[name=movie-title]').value;
  returnedMovie.Rating = document.querySelector('input[name=rating]').value;
  returnedMovie.Username = document.querySelector('input[name=username]').value;
  return JSON.stringify(returnedMovie);
}


function init(data) {
  movieData = data;
  let myUl = document.createElement('ul');
  movieData.forEach(function(movie, index){
    let myLi = document.createElement('li');
    dataView.appendChild(myUl);
    dataView.appendChild(myLi);
    myLi.textContent ='Movie: ' +data[index].MovieTitle +', '+'Rating: '+data[index].Rating+', '+'Username: '+data[index].Username;
  });

}
