/**
 * Control Panel module
 * by Tibor's way
 * Methods
 *  - play(url)
 *  - next
 *  - previous
 */
 var ControlPanel = (function () {
 	var trackDir = './tracks/';
 	var root = document.querySelector('.mscplayer');
 	var prevButton = root.querySelector('.reverse');
 	var nextButton = root.querySelector('.forward');
 	var playButton = root.querySelector('.play');
 	var seekBar = root.querySelector('input');
 	var timerLabel = root.querySelector('.currentTime');
 	var loadButton = document.querySelector('.star'); // This is temporary
  playButton.className = 'play';
  var counter = 0;

  // trackNameList = [];

 // 	loadButton.addEventListener('click', function(){
 // 		load('music.mp3');
 // 		console.log('loaded');
 // 	});

 	playButton.addEventListener('click', function(){
    // this.className = 'play';
 		if( Audio.paused() ){
 			this.className = 'pause';
 			Audio.play();
 		} else {
 			this.className = 'play';
 			Audio.pause();
 		}
 	});

  nextButton.addEventListener('click', function(){
    counter++;
    // console.log(Tracks.tracks().length);
    if ( counter > Tracks.tracks().length) {
      counter = 0;
    }
    loadM(counter);
  });

  prevButton.addEventListener('click', function(){
    counter--;
    if (counter < 0) {
      counter = Tracks.tracks().length-1;
    }
    loadM(counter);
  });

 	function loadM() {
    // console.log(Tracks.tracks());
    // console.log(Tracks.tracks());
    console.log(counter);
		Audio.load(Tracks.tracks()[counter].fileName);
    // Audio.play();
		Audio.onUpdate(function( percent, time ){
			seekBar.rangeSlider.update({value: percent});
			timerLabel.innerHTML = format(time);
		});
 	}

	function format(s) {
        var s = Math.floor((s) % 60);
        if (s < 10) { s = "0"+s; }
        return Math.floor(s/60) + ":" + s;
	}

  function setCounter(param) {
    counter = param;
  }
 //  function init(){
 //   ajax.getTracks(null, function(res){
 //     trackNameList = res;
 //     console.log(res.fileName);
 //   })
 // }

  setTimeout(loadM, 50);

 	return {
 		load: loadM,
    setCounter: setCounter
 	}

 })();

// ControlPanel.init();
