function Ajax() {
  let xhr = new XMLHttpRequest();
  let url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
  this.get = function() {
    xhr.open('GET', url, true);
    xhr.send();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        console.log(JSON.parse(xhr.response));
        // console.log(this);
        return (JSON.parse(xhr.response));
      }
    }
  }
  this.update = function() {
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
  }
}

let server = new Ajax();
console.log(server.get());
// console.log(this);
