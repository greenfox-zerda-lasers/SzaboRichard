/**
 * Audio module
 * by Tibor's way
 * Methods
 *  - load( url )
 *  - play
 *  - pause
 *  - seek
 *  - volume( 0-100 )
 * Events
 *  - timeupdate: fires when music is playing
 *  - ended: fires when currentTime is duration
 */
var Audio = (function () {
	var audioNode = document.createElement('audio');
	var timeCallback = function(){};
	var endCallback = function(){};
  var ajax = new Ajax();
  // var currTimeCallback = function(){};

	audioNode.addEventListener('timeupdate', function(){
		var percent = audioNode.currentTime / audioNode.duration * 100;
		timeCallback( percent, audioNode.currentTime );
	});

	audioNode.addEventListener('ended', function(){
		endCallback();
	});

	function setUpdateEvent( cb ) {
		timeCallback = cb;
	}

	function setCompleteEvent( cb ) {
		endCallback = cb;
	}

	function load( url ) {
		audioNode.src = './tracks/' + url;
    // ajax.
    // var trackDir = './tracks/';
	}

	function play(){
		audioNode.play();
    // Tracks.tracks
	}

	function pause(){
		audioNode.pause();
	}

	// expects between 0-100 value
	function seek( percent ){
		audioNode.currentTime = audioNode.duration * percent / 100;
	}

  function currTimeUpdate ( percent, position) {
    return audioNode.currentTime;
  }

	function isPaused() {
		return audioNode.paused;
	}

	return {
		load: load,
		play: play,
		pause: pause,
		seek: seek,
		onUpdate: setUpdateEvent,
		onComplete: setCompleteEvent,
    timeUpdate: currTimeUpdate,
		paused: isPaused
	}
})();
