"use strict";

describe("pow", function() {
    it("2 raised to the power 3 is 8", function() {
        assert.equal( pow(2,3), 8);
    });
});

describe("draw", function() {
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


describe("request", function() {
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


