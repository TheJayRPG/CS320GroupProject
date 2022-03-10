"use strict";

let ROWS = 20;
let COLS = 20;


let drawer = new ConwayDrawer(ROWS,COLS, GRIDTYPE.SQUARE, ROWS, COLS);
let thisTime = Date.now();
let prevTime
const frameRate = 60;


function draw() {
    prevTime = thisTime;
    thisTime = Date.now();
    drawer.draw( thisTime - prevTime);
}
//drawer.setMoveWindow(95,95);
setInterval(draw, 1000/frameRate);
//setInterval(()=>drawer.moveWindow(0,1),1000);
setInterval(getServerTiles, 250);
//window.requestAnimationFrame(()=>drawer.draw());
function pow(a,b) {
    return a**b;
}
