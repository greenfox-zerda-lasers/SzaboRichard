let musiclist = ['./music/Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3', './music/Ars_Sonor_-_02_-_Never_Give_Up.mp3']
let media = document.querySelector('audio');
let play = document.querySelector('.pause');
let reverse = document.querySelector('.reverse');
let forward = document.querySelector('.forward');
let counter = 0;
media.setAttribute('src', musiclist[counter]);

play.addEventListener('click', function(){
  if(media.paused)
  {
    media.play();
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
    counter = musiclist.length-1;
  }
  media.setAttribute('src', musiclist[counter]);
  media.play();
});

forward.addEventListener('click', function(){
  counter++;
  if (counter > musiclist.length) {
    counter = 0;
  }
  console.log(musiclist[counter]);
  media.setAttribute('src', musiclist[counter]);
  media.play();
})
