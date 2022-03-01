"use strict";
let drawer = new ConwayDrawer(1000,1000);
let thisTime = Date.now();
let prevTime
const frameRate = 60;

function draw() {
    prevTime = thisTime;
    thisTime = Date.now();
    drawer.draw( thisTime - prevTime);
}

setInterval(draw, 1000/frameRate);
//window.requestAnimationFrame(()=>drawer.draw());

function pow(a,b) {
    return a**b;
}
