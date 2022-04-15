"use strict";

describe("pow", function() {    //Meta Test
    it("2 raised to the power 3 is 8", function() {
        assert.equal( pow(2,3), 8);
    });
});

describe("draw", function() {   // Acceptance Test
    let EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
    let runsArr = [];
    const runCount = 100;
    const runMaxTime = 5;
    for(let i = 0; i < runCount; i++) {
            let start = Date.now();
            EmptyDrawer.draw(0);
            runsArr.push(Date.now() - start); 
    }
    it(`All ${runCount} runs within ${runMaxTime}ms`, function() {
        assert(Math.max(...runsArr) < 5);
    });
});


describe("draw graph edges", function() {   // Branch Coverage Test
    let EmptyDrawer;
    function drawCommon() {
        EmptyDrawer.draw(0);
        let gl = EmptyDrawer._gl;
        let pixels = new Uint8Array(4);
        let aliveArr = new Array();
        let tileSet = EmptyDrawer.getTiles().flat();
        

        for(let y = 0; y < EmptyDrawer.rangeY; y++) {
            for(let x = 0; x < EmptyDrawer.rangeX; x++) {
                //gl.readPixels(400 / EmptyDrawer.rangeX * x, 400 / EmptyDrawer.rangeY * y, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, pixels);
                gl.readPixels(400 * x / EmptyDrawer.rangeX + 1, 400 * y / EmptyDrawer.rangeY + 1, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, pixels);
                aliveArr.push(pixels[0]/255);
                //console.log(tileSet.pop());
                //aliveArr.push(pixels[0]);
            }
        }
        //alert(tileSet);
        //alert(aliveArr);
        for(let i = 0; i < EmptyDrawer.rangeX * EmptyDrawer.rangeY; i++) {
            if(tileSet[i] != (aliveArr[i]) ) {
                console.log(`${i} ${tileSet[i]} ${aliveArr[i]}`);
                assert(false);
            }
        }
        assert(true);
    }
    it("Case where selection within grid", function() {
        EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
        drawCommon();
    });
    it("Case where selection passes xMax", function() {
        EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
        EmptyDrawer.setMoveWindow(95,0);
        drawCommon();
    });
    it("Case where selection passes yMax", function() {
        EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
        EmptyDrawer.setMoveWindow(0,95);
        drawCommon();
    });
    it("Case where selection passes xMax and yMax", function() {
        EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
        EmptyDrawer.setMoveWindow(95,95);
        drawCommon();
    });
});

describe("request", function(){     // Integration Test
    it("Request goes through", function() {
        assert(getServerTiles().length > 0);
    });
});

describe("swap gridtype", function(){   // Acceptance Test
    it("swap back gridtype works", function() {
        let EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
        EmptyDrawer.swapGridType(GRIDTYPE.TEST);
        EmptyDrawer.swapGridType(GRIDTYPE.SQUARE);
        assert(EmptyDrawer.gridType == GRIDTYPE.SQUARE);
    });
});
describe("move grid position", function(){   // Acceptance Test
    it("move", function() {
        let EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
        const offX = 1;
        const offY = 2;
        const oldPosX = EmptyDrawer.posX;
        const oldPosY = EmptyDrawer.posY;
        EmptyDrawer.moveWindow(offX, offY);
        assert(((EmptyDrawer.posX - offX) % EmptyDrawer.maxX == oldPosX) && ((EmptyDrawer.posY - offY) % EmptyDrawer.maxY == oldPosY));
    });
    it("move above max", function() {
        let EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
        const offX = EmptyDrawer.maxX + 2;
        const offY = EmptyDrawer.maxY + 3;
        const oldPosX = EmptyDrawer.posX;
        const oldPosY = EmptyDrawer.posY;
        EmptyDrawer.moveWindow(offX, offY);
        assert(((EmptyDrawer.posX - offX) % EmptyDrawer.maxX == oldPosX) && ((EmptyDrawer.posY - offY) % EmptyDrawer.maxY == oldPosY));
    });
    it("move below min", function() {
        let EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
        const offX = - EmptyDrawer.maxX - 2;
        const offY = - EmptyDrawer.maxY - 3;
        const oldPosX = EmptyDrawer.posX;
        const oldPosY = EmptyDrawer.posY;
        EmptyDrawer.moveWindow(offX, offY);
        assert(((EmptyDrawer.posX - offX) % EmptyDrawer.maxX == oldPosX) && ((EmptyDrawer.posY - offY) % EmptyDrawer.maxY == oldPosY));
    });
});

describe("scale grid size", function(){   // Acceptance Test
    it("scale", function() {
        let EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
        const offX = 1;
        const offY = offX;
        const oldPosX = EmptyDrawer.rangeX;
        const oldPosY = EmptyDrawer.rangeY;
        EmptyDrawer.scaleWindow(offX);
        const corX = Math.min(EmptyDrawer.maxX, Math.max(oldPosX + offX, 1));
        const corY = Math.min(EmptyDrawer.maxY, Math.max(oldPosY + offY, 1));
        assert((corX == EmptyDrawer.rangeX) && (corY == EmptyDrawer.rangeY));
    });
    it("scale above max", function() {
        let EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
        const offX = EmptyDrawer.maxX + 2;
        const offY = offX;
        const oldPosX = EmptyDrawer.rangeX;
        const oldPosY = EmptyDrawer.rangeY;
        EmptyDrawer.scaleWindow(offX);
        const corX = Math.min(EmptyDrawer.maxX, Math.max(oldPosX + offX, 1));
        const corY = Math.min(EmptyDrawer.maxY, Math.max(oldPosY + offY, 1));
        assert((corX == EmptyDrawer.rangeX) && (corY == EmptyDrawer.rangeY));
    });
    it("scale below min", function() {
        let EmptyDrawer = new ConwayDrawer(100,100, GRIDTYPE.SQUARE, 7, 11);
        const offX = - EmptyDrawer.maxX - 2;
        const offY = offX;
        const oldPosX = EmptyDrawer.rangeX;
        const oldPosY = EmptyDrawer.rangeY;
        EmptyDrawer.scaleWindow(offX);
        const corX = Math.min(EmptyDrawer.maxX, Math.max(oldPosX + offX, 1));
        const corY = Math.min(EmptyDrawer.maxY, Math.max(oldPosY + offY, 1));
        assert((corX == EmptyDrawer.rangeX) && (corY == EmptyDrawer.rangeY));
    });
});

