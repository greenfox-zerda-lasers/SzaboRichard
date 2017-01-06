/**
 *Track module
 *by Tibi's way
 *render
 *delete
 *get tracks
 *ajad

 **/

 var Tracks = (function() {
   var root = document.querySelector('.tracks');
   var img = document.querySelector('img');
   var trackslist = [];
   var ajax = new Ajax();
   var counter = 0;

   function render(){
     trackslist.forEach(function(track){
       counter++;
       var trackData = _createTracklistItem(counter, track.title, track.duration);
      //  console.log(track);
       var divNode = document.createElement('div');
       divNode.dataset.id = counter;
       divNode.addEventListener('click', function(){
         ControlPanel.setCounter( divNode.dataset.id-1);
         ControlPanel.load();
        //  Audio.play();
        //  img.src = thsi.track.
       });
       var divNodeInner = document.createElement('div');
       divNodeInner.className = 'tracklist-inner-style';
       divNode.className = 'tracklist-inner';
       root.appendChild(divNode);
       divNode.appendChild(divNodeInner);
       divNodeInner.appendChild(trackData[0])
       divNodeInner.appendChild(trackData[1])
       divNode.appendChild(trackData[2]);
       if (counter % 2 === 0) {
         divNode.className = 'tracklist-inner lightergray';
       }
     })
     Audio.load(trackslist[0].fileName)
   };

   function _createTracklistItem( counter, name, time) {
     var p = document.createElement('p');
     var trackP = document.createElement('p');
     var timerP = document.createElement('p');
    //  console.log(id, name, time);
     p.textContent = counter;
     trackP.textContent = name;
     timerP.textContent = time;
     return [p, trackP, timerP];
   }

   function lister() {
     return trackslist;
   }

   return {
     init: function(){
       ajax.getTracks(null, function(res){
         trackslist = res;
        //  console.log(trackslist);
         render();
       })
     },
     tracks: lister
   }
 }) ();

Tracks.init();
console.log(Tracks.tracks());
