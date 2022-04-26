"use strict";

function handleSize() {
    socket.emit('get_grid_size', function(response) {
        //console.log(response);
        let gsize = JSON.parse(response);
//console.log(gsize);
let ROWS = gsize[0];
let COLS = gsize[1];

withinTestingEnvironment = false
let drawer = new ConwayDrawer(ROWS,COLS, GRIDTYPE.SQUARE, 10, 10);

let thisTime = Date.now();
let prevTime
const frameRate = 60;


function draw() {
    prevTime = thisTime;
    thisTime = Date.now();
    if(hasUpdate) {
        drawer.draw( thisTime - prevTime);
    }
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
    if(event.which == 1) {
        if (Math.abs(diffX) < delta && Math.abs(diffY) < delta) {
            let rect = drawer._canvas.getBoundingClientRect();
            //console.log("click " + (event.pageX-rect.x) + ", " + (event.pageY-rect.y));

            console.log("click: " + (drawer.posX+Math.trunc((event.pageX-rect.x) * drawer.rangeX / 400))%drawer.maxX+", "+(drawer.posY+drawer.rangeY-Math.trunc((event.pageY-rect.y) * drawer.rangeY / 400)-1)%drawer.maxY);
            console.log(`[${drawer.posX},${drawer.posY}]`);
            flipTile((drawer.posX+Math.trunc((event.pageX-rect.x) * drawer.rangeX / 400))%drawer.maxX,(drawer.posY+drawer.rangeY-Math.trunc((event.pageY-rect.y) * drawer.rangeY / 400)-1)%drawer.maxY);

        } else {
            console.log("drag: " + Math.round(diffX * drawer.rangeX / 400) + " " + -Math.round(diffY * drawer.rangeY / 400));
            drawer.moveWindow(-Math.round(diffX * drawer.rangeX / 400),Math.round(diffY * drawer.rangeY / 400));
            //console.log("drag " + diffX + " " + diffY);
        }
    }
});



//END: https://stackoverflow.com/questions/6042202/how-to-distinguish-mouse-click-and-drag


// https://www.section.io/engineering-education/keyboard-events-in-javascript/
document.addEventListener('keypress', function (event) {
    console.log(event.key + " pressed!");
    if(event.key == "1") {
        drawer.swapGridType(GRIDTYPE.TEST);
    } else if(event.key == "2") {
        drawer.swapGridType(GRIDTYPE.SQUARE);
    } else if(event.key == "3") {
        drawer.swapGridType(GRIDTYPE.SQUARE_ANIM);
    } else if(event.key == "4") {
        drawer.swapGridType(GRIDTYPE.SQUARE_DIFF);
    }

});
let scaleDelta = 0;
element.addEventListener('wheel', function (event) {
    event.preventDefault();
    console.log('did scroll ' + event.deltaY + " " + scaleDelta);
    scaleDelta = scaleDelta + event.deltaY;
    drawer.scaleWindow(Math.trunc(scaleDelta/100));
    scaleDelta = scaleDelta - Math.trunc(scaleDelta/100)*100;
});

element.addEventListener('contextmenu', function(event) {
    event.preventDefault();
    let rect = drawer._canvas.getBoundingClientRect();
    console.log("right click: " + (drawer.posX+Math.trunc((event.pageX-rect.x) * drawer.rangeX / 400))%drawer.maxX+", "+(drawer.posY+drawer.rangeY-Math.trunc((event.pageY-rect.y) * drawer.rangeY / 400)-1)%drawer.maxY);
    console.log(`[${drawer.posX},${drawer.posY}]`);
    displayStatus(event.pageX,event.pageY,(drawer.posX+Math.trunc((event.pageX-rect.x) * drawer.rangeX / 400))%drawer.maxX,(drawer.posY+drawer.rangeY-Math.trunc((event.pageY-rect.y) * drawer.rangeY / 400)-1)%drawer.maxY);
});

/* https://itnext.io/how-to-create-a-custom-right-click-menu-with-javascript-9c368bb58724 */
document.addEventListener("click", (event) => {
    const contextMenu = document.getElementById("context-menu");
    contextMenu.classList.remove("visible");
});


//drawer.setMoveWindow(95,95);
setInterval(draw, 1000/frameRate);
//setInterval(()=>drawer.moveWindow(0,1),1000);
//setInterval(getServerTiles, 250);
//window.requestAnimationFrame(()=>drawer.draw());
//print();
});
}
function pow(a,b) {
    return a**b;
}
handleSize();