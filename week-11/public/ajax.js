var Ajax = function(){
  this.APIEndpoint = 'http://localhost:3600/';

  this.getData = function(callback) {
    this.open('GET', false, 'decode/all', callback);
  }

  this.decodeData = function(data, callback) {
    this.open('POST', data, 'decode/', callback);
  }

  this.deleteData = function(data, callback, index) {
    this.open('DELETE', data, 'delete/', callback, index);
  }

  this.open = function(method, data, resource, callback) {
    var xhr = new XMLHttpRequest();
    data = (data) ? data : null;
    xhr.open( method, this.APIEndpoint + resource)

    if (method !== 'DELETE') {
      xhr.setRequestHeader('Content-Type', 'application/json');
    }
    else {
      xhr.open( method, this.APIEndpoint + index);
    }

    xhr.send( JSON.stringify(data));
    xhr.onreadystatechange = function (rsp) {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if ( xhr.status === 200 ) {
          console.log(xhr.responseText);
          callback( JSON.parse(xhr.response));
        } else {
          alert('There was a problem with the connection!');
        }
      }
    }
  }
}
