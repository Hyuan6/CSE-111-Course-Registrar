document.getElementById("queueNumber").text = ""; //Math.floor((Math.random() * 100) + 1);

var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;

function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '0',
        width: '0',
        videoId: '5qap5aO4i9A',
    });
}

var playEmbeddedVideo = true;

function toggleVideo() {
    if (playEmbeddedVideo) {
        player.playVideo();
        document.getElementById("playButton").src = pauseButton;
    } else {
        player.stopVideo();
        document.getElementById("playButton").src = playButton;
    }
    playEmbeddedVideo = !playEmbeddedVideo;
}

const buttons = document.querySelectorAll("#audioPanel #audioButton");
buttons.forEach(el => {
    const span = el.lastElementChild;
    const width = span.offsetWidth;
    span.style.width = 0;
    el.addEventListener("mouseenter", () => {
        span.style.width = `${width}px`;
    });
    el.addEventListener("mouseleave", () => {
        span.style.width = 0;
    });
});

// var minutes = 1.5;

// function bannerCounter() {

//     var min = 1,
//         max = 10;
//     var rand = Math.floor(Math.random() * (max - min + 1) + min);
//     var newVal = Math.max(parseInt(document.querySelector("#queueNumber").text) - rand, 0);
//     document.querySelector("#queueNumber").text = newVal;

//     // if (newVal == 0){
//     // 	window.location.href = "/LegReg/submit";
//     // }

//     max = 30;
//     rand = Math.floor(Math.random() * (max - min + 1) + min);
//     setTimeout(bannerCounter, rand * 1000);
// }

// bannerCounter();