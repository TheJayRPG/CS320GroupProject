"use strict";

let drawer = new ConwayDrawer(1000,1000, GRIDTYPE.SQUARE, 10, 10);
let thisTime = Date.now();
let prevTime
const frameRate = 60;

function requestTiles(minX, minY, maxX, maxY) {
    return [
        [  0,255,255,255,255,  0,255,255,255,255],
        [  0,255,255,255,255,  0,255,255,255,  0],
        [  0,255,  0,255,255,  0,255,255,255,255],
        [  0,255,255,255,255,  0,255,255,255,255],
        [  0,255,255,255,255,  0,255,255,255,255],
        [  0,255,255,255,255,  0,255,255,255,255],
        [  0,255,255,  0,255,  0,255,255,255,255],
        [  0,255,255,255,255,  0,255,255,255,255],
        [  0,255,255,255,255,  0,255,  0,255,255],
        [  0,255,255,255,255,  0,255,255,255,255],
    ];
}



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
