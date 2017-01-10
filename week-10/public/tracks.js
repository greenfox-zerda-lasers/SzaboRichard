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
     sec = Math.floor( time );
     min = Math.floor( sec / 60 );
     min = min >= 10 ? min : '0' + min;
     sec = Math.floor( sec % 60 );
     sec = sec >= 10 ? sec : '0' + sec;
     p.textContent = counter;
     trackP.textContent = name;
     timerP.textContent = min + ':' + sec;
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
