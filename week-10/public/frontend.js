let musicList = ['./music/Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3', './music/Ars_Sonor_-_02_-_Never_Give_Up.mp3']
let media = document.querySelector('audio');
let play = document.querySelector('.pause');
let reverse = document.querySelector('.reverse');
let forward = document.querySelector('.forward');
let counter = 0;
let currTime = document.querySelector('.currentTime');
let setTrackAndPlay = function mediaPlayer(index) {
  media.setAttribute('src', musicList[index]);
  media.play();
};



// media.addEventListener('canplaythrough', function() {
//     this.currentTime = 12;
//     this.play();
// });

media.addEventListener('timeupdate',function(){
    var currentTimeMs = media.currentTime;
    let musicTime = function readableDuration(seconds) {
       sec = Math.floor( seconds );
       min = Math.floor( sec / 60 );
       min = min >= 10 ? min : '0' + min;
       sec = Math.floor( sec % 60 );
       sec = sec >= 10 ? sec : '0' + sec;
       return min + ':' + sec;
    }
    console.log(musicTime(currentTimeMs));
    currTime.textContent = musicTime(currentTimeMs);
},false);

play.addEventListener('click', function(){
  if(media.paused)
  {
    setTrackAndPlay(counter);
    console.log('play');
  }
  else
  {
    media.pause();
    console.log('paused');
  }
}, false);

reverse.addEventListener('click', function(){
  counter--;
  if (counter < 0) {
    counter = musicList.length-1;
  }
  setTrackAndPlay(counter);
});

forward.addEventListener('click', function(){
  counter++;
  if (counter > musicList.length-1) {
    counter = 0;
  }
  // console.log('for ' + counter);
  setTrackAndPlay(counter);
})
