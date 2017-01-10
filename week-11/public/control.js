var Control = (function(){
  var button = document.querySelector('button');
  var loading = document.querySelector('span');
  var textInput = document.querySelector('textarea');
  var numberInput = document.querySelector('input[type=number]');
  var ajax = new Ajax();

  button.addEventListener('click', function(){
    var returnedData = {};
    returnedData.text = textInput.value;
    returnedData.shift = numberInput.value;
    // console.log(returnedData);
    loading.textContent = "LOADED";
    sendData(returnedData);
    // returnedData.text, returnedData.shift = "";
  });

  function sendData(collectedData) {
    ajax.decodeData(collectedData, function(res){
      loading.textContent = "";
    })
  }

})();
