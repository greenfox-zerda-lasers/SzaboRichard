/**
 * Control Panel module
 * by Tibor's way
 * Methods
 *  - play(url)
 *  - next
 *  - previous
 */
 var ControlPanel = (function () {
 	var trackDir = 'C:/Users/ignoc/Desktop/Greenfox/SzaboRichard/week-10/server/music/';
 	var root = document.querySelector('.mscplayer');
 	var prevButton = root.querySelector('.reverse');
 	var nextButton = root.querySelector('.forward');
 	var playButton = root.querySelector('.play');
 	var seekBar = root.querySelector('input');
 	var timerLabel = root.querySelector('.currentTime');
 	var loadButton = document.querySelector('.star'); // This is temporary

 	loadButton.addEventListener('click', function(){
 		load('music.mp3');
 		console.log('loaded');
 	});

 	playButton.addEventListener('click', function(){
 		if( Audio.paused() ){
 			this.className = 'pause';
 			Audio.play();
 		} else {
 			this.className = 'play';
 			Audio.pause();
 		}
 	});

 	function load(fileName) {
		Audio.load(trackDir + fileName);

		Audio.onUpdate(function( percent, time ){
			seekBar.rangeSlider.update({value: percent});
			timerLabel.innerHTML = format(time);
		});
		// audio.onComplete(function(){
		// 	console.log('READY');
		// });
 	}

	function format(s) {
        var s = Math.floor((s) % 60);
        if (s < 10) { s = "0"+s; }
        return Math.floor(s/60) + ":" + s;
	}

 	return {
 		// play: play
 	}

 })();
