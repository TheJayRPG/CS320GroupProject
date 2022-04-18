"use strict";

let ROWS = 20;
let COLS = 20;

withinTestingEnvironment = false
let drawer = new ConwayDrawer(ROWS,COLS, GRIDTYPE.SQUARE, ROWS, COLS);

let thisTime = Date.now();
let prevTime
const frameRate = 60;


function draw() {
    prevTime = thisTime;
    thisTime = Date.now();
    drawer.draw( thisTime - prevTime);
    //console.log(reallyLongNameForStorageOfTile);
}

//BEGIN: https://stackoverflow.com/questions/6042202/how-to-distinguish-mouse-click-and-drag
const delta = 6;
let startX;
let startY;
let element = drawer.getCanvas();

element.addEventListener('mousedown', function (event) {
  startX = event.pageX;
  startY = event.pageY;
});

element.addEventListener('mouseup', function (event) {
    const diffX = (event.pageX - startX);
    const diffY = (event.pageY - startY);

    if (Math.abs(diffX) < delta && Math.abs(diffY) < delta) {
        console.log("click");
    } else {
        console.log("" + Math.trunc(diffX * drawer.rangeX / 400) + " " + -Math.trunc(diffY * drawer.rangeY / 400));
        drawer.moveWindow(-Math.trunc(diffX * drawer.rangeX / 400),Math.trunc(diffY * drawer.rangeY / 400));
        //console.log("drag " + diffX + " " + diffY);
    }
});



//END: https://stackoverflow.com/questions/6042202/how-to-distinguish-mouse-click-and-drag


// https://www.section.io/engineering-education/keyboard-events-in-javascript/
document.addEventListener('keypress', function (event) {
    console.log(event.key + " pressed!");

});

element.addEventListener('wheel', function (event) {
    console.log('did scroll');
});


//drawer.setMoveWindow(95,95);
setInterval(draw, 1000/frameRate);
//setInterval(()=>drawer.moveWindow(0,1),1000);
//setInterval(getServerTiles, 250);
//window.requestAnimationFrame(()=>drawer.draw());
function pow(a,b) {
    return a**b;
}
