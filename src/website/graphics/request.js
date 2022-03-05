"use strict"
let reallyLongNameForStorageOfTiles = [];
initRequestTiles();

function initRequestTiles() {
    for(let x = 0; x < 100; x++) {
        reallyLongNameForStorageOfTiles.push([]);
        for(let y = 0; y < 100; y++) {
            if(Math.random() >= 0.2) {
                reallyLongNameForStorageOfTiles[x].push(1);
            } else {
                reallyLongNameForStorageOfTiles[x].push(0);
            }
        }
    }
}

function requestTiles(minX, minY, maxX, maxY) {
    //console.log(`${minX} ${maxX} ${minY} ${maxY}`);
    
    let shortName = reallyLongNameForStorageOfTiles
        .slice(minY, maxY)
        .map(y => y.slice(minX, maxX));
    
    //console.log(`${shortName[0][0]} ${reallyLongNameForStorageOfTiles[minX][minY]}`);
    return shortName;
}