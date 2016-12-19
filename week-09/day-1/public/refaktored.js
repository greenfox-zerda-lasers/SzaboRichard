function Ajax() {
  this.xhr = new XMLHttpRequest();
  this.url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
}

function App() {
  this.init = function() {
    this.ajax = new Ajax();
    this.ajax.connect(this.renfer)

  }
  this.render = ...
}

Ajax.prottype.conncect = function(xhrReq, index, headerText, data,cb) {
    this.xhr.open(xhrReq, url+index, true);
    this.xhr.send();
    this.xhr.onreadystatechange = function() {
      if (this.xhr.readyState === XMLHttpRequest.DONE) {
        // console.log(JSON.parse(this.xhr.response));
        // console.log(this);
        cb(JSON.parse(this.xhr.response));
      }
    }
  }



// let server = new Ajax();
// console.log(server.get());
// console.log(this);
