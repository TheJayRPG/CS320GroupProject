"use strict";

describe("pow", function() {
    it("2 raised to the power 3 is 8", function() {
        assert.equal( pow(2,3), 8);
    });
});

describe("draw", function() {
    let EmptyDrawer = new ConwayDrawer(1000,1000, GRIDTYPE.SQUARE, 10, 10);
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
    let EmptyDrawer = new ConwayDrawer(1000,1000, GRIDTYPE.SQUARE, 10, 10);
    EmptyDrawer.draw(0);
    let gl = EmptyDrawer._gl;
    let pixels = new Uint8Array(4);
    let aliveArr = new Array();
    let tileSet = requestTiles().flat();
    for(let x = 0; x < EmptyDrawer.rangeX; x++) {
        for(let y = 0; y < EmptyDrawer.rangeY; y++) {
            gl.readPixels(400 / EmptyDrawer.rangeY * y, 400 / EmptyDrawer.rangeX * x, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, pixels);
            aliveArr.push(pixels[0]);
            //console.log(aliveArr.pop());
            //aliveArr.push(pixels[0]);
        }
    }
    it(`All pixels are correct`, function() {
        for(let i = 0; i < EmptyDrawer.rangeX * EmptyDrawer.rangeY; i++) {
            if(tileSet[i] != (aliveArr[i] / 255) ) {
                console.log(`${i} ${tileSet[i]} ${aliveArr[i] / 255}`);
                assert(false);
            }
        }
        assert(true);
    });
});
