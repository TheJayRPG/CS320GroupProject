"use strict"
//let reallyLongNameForStorageOfTiles = [];
//initRequestTiles();
/*
function initRequestTiles() {
    for(let x = 0; x < 100; x++) {
        reallyLongNameForStorageOfTiles.push([]);
        for(let y = 0; y < 100; y++) {
            if(Math.random() >= 0.0) {
                reallyLongNameForStorageOfTiles[x].push(1);
            } else {
                reallyLongNameForStorageOfTiles[x].push(0);
            }
        }
    }
}
*/

function loadFile(filePath) {       //https://stackoverflow.com/questions/36921947/read-a-server-side-file-using-javascript
    var result = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", filePath, false);
    xmlhttp.send();
    if(xmlhttp.status == 200) {
        result = xmlhttp.responseText;
    }
    return result;
}
/*
function getServerTiles() {
    var result = null;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("POST", "TILES", false);
    xmlhttp.send();
    if(xmlhttp.status == 200) {
        result = xmlhttp.responseText;
    }
    //console.log(result);
    
    reallyLongNameForStorageOfTiles = JSON.parse(result);
    //console.log(reallyLongNameForStorageOfTiles);
    //console.log(reallyLongNameForStorageOfTiles);
    //alert(reallyLongNameForStorageOfTiles);
    return result;
}*/


function requestTiles(minX, minY, maxX, maxY) {
    //console.log(`${minX} ${maxX} ${minY} ${maxY}`);
    
    let result = serverTiles
        .slice(minY, maxY)
        .map(y => y.slice(minX, maxX));
    
    //console.log(`${result[0][0]} ${reallyLongNameForStorageOfTiles[minX][minY]}`);
    return result;
}

/*
function getServerTiles(result) {
    if(hasUpdate) {
        reallyLongNameForStorageOfTiles = serverTiles;
    }
    //console.log(reallyLongNameForStorageOfTiles);
    //console.log(reallyLongNameForStorageOfTiles);
    //alert(reallyLongNameForStorageOfTiles);
    return result;
}
*/

