var RenderIncData = ( function(){
  var root = document.querySelector('ol');
  var messages = [];
  var ajax = new Ajax();

  function render(){
    messages.forEach(function(msg, index){
      var liItem = document.createElement('li');
      root.appendChild(liItem)
      // console.log(index);
      // console.log(msg);
      // console.log(msg[index]);
      liItem.textContent = msg;
    })
  };

  return {
    init: function(){
      ajax.getData(function(res){
        // console.log(res);
        messages = res.all;
        render();
      })
    }
  }
}) ();

RenderIncData.init();
