"use strict";

let drawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
let thisTime = Date.now();
let prevTime
const frameRate = 60;


function draw() {
    prevTime = thisTime;
    thisTime = Date.now();
    drawer.draw( thisTime - prevTime);
}
drawer.setMoveWindow(95,95);
setInterval(draw, 1000/frameRate);
setInterval(()=>drawer.moveWindow(0,1),1000);
//window.requestAnimationFrame(()=>drawer.draw());
function pow(a,b) {
    return a**b;
}
