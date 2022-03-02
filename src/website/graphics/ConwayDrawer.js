"use strict";
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

function requestTiles(minX, minY, maxX, maxY) {
    return [
        [0,1,1,1,1,  0,1,1,1,1],
        [0,1,1,1,1,  0,1,1,1,0],
        [0,1,0,1,1,  0,1,1,1,1],
        [0,1,1,1,1,  0,1,1,1,1],
        [0,1,1,1,1,  0,1,1,1,1],
        [0,1,1,1,1,  0,1,1,1,1],
        [0,1,1,0,1,  0,1,1,1,1],
        [0,1,1,1,1,  0,1,1,1,1],
        [0,1,1,1,1,  0,1,0,1,1],
        [0,1,1,1,1,  0,1,1,1,1],
    ];
}

const GRIDTYPE = { 
    SQUARE: {
        DRAW(gl, _thisArg) {
            if(typeof _thisArg === 'undefined') throw new Error("You forgot _thisArg!");
            gl.clearColor(0.0,0.0,0.0,1.0);
            gl.clearDepth(1.0);
            gl.enable(gl.DEPTH_TEST);
            gl.depthFunc(gl.LEQUAL);
            gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
            gl.bindBuffer(gl.ARRAY_BUFFER, _thisArg.buffers.position);
            let numComponents = 2;
            let type = gl.FLOAT;
            let normalize = false;
            let stride = 0;
                                      
            let offset = 0;
            gl.vertexAttribPointer(
                _thisArg.atPos1,
                numComponents,
                type,
                normalize,
                stride,
                offset);
            /*
            gl.bindBuffer(gl.ARRAY_BUFFER, _thisArg.buffers.conway);
            let tileState = _thisArg.getTiles();
            gl.bufferData(gl.ARRAY_BUFFER, new Uint8Array(tileState), gl.STREAM_DRAW);
            numComponents = 1;
            type = gl.BYTE;
            normalize = false;
            stride = 0;
                                      
            offset = 0;
            gl.vertexAttribPointer(
                _thisArg.atPos2,
                numComponents,
                type,
                normalize,
                stride,
                offset);
            */
            gl.bindTexture(gl.TEXTURE_2D, _thisArg.buffers.texture);
            //START: https://webglfundamentals.org/webgl/lessons/webgl-data-textures.html
            //let tileState = _thisArg.getTiles();    
            let tileState = _thisArg.getTiles();
            const level = 0;
            const internalFormat = gl.LUMINANCE;
            const width = _thisArg.rangeX;
            const height = _thisArg.rangeY;
            const border = 0;
            const format = gl.LUMINANCE;
            const fType = gl.UNSIGNED_BYTE;
            const data = new Uint8Array(tileState.flat().map((x)=>255*x));
            //alert(data.length);
            gl.texImage2D(gl.TEXTURE_2D, level, internalFormat, width, height, border,
                format, fType, data);
   
            const alignment = 1;
            gl.pixelStorei(gl.UNPACK_ALIGNMENT, alignment);
            // set the filtering so we don't need mips and it's not filtered
            gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
            gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
            gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
            gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);

            //END: https://webglfundamentals.org/webgl/lessons/webgl-data-textures.html
            gl.enableVertexAttribArray(_thisArg.atPos1);
            //gl.enableVertexAttribArray(_thisArg.atPos2);
            gl.useProgram(_thisArg.shaderProgram);
            //gl.uniform1f(_thisArg.unPos1, Math.floor(_thisArg.netTime) / 1000);
            //console.log(this.netTime);
            const offset2 = 0;
            const vertexCount = 4;
            gl.drawArrays(gl.TRIANGLE_STRIP, offset, vertexCount);
        },
        SETUP(gl, _thisArg) {
            if(typeof _thisArg === 'undefined') throw new Error("You forgot _thisArg!");
            const fragmentShader = loadFile("./shaders/square.frag");
            const vertexShader = loadFile("./shaders/square.vert");
            _thisArg.shaderProgram = _thisArg._createSimpleShader(_thisArg._gl, vertexShader, fragmentShader);            
            _thisArg.atPos1 = gl.getAttribLocation(_thisArg.shaderProgram, 'aVertexPosition');
            //_thisArg.atPos2 = gl.getAttribLocation(_thisArg.shaderProgram, 'a_texcoord');
            const positions = [
                1.0,  1.0,
               -1.0,  1.0,
                1.0, -1.0,
               -1.0, -1.0,
           ];
           const positionBuffer = gl.createBuffer();
           gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
           gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(positions), gl.STATIC_DRAW);
           //const conwayBuffer = gl.createBuffer();
           const textureBuffer = gl.createTexture();
           gl.bindTexture(gl.TEXTURE_2D, _thisArg.textureBuffer);

           _thisArg.buffers = {
               position: positionBuffer,
               //conway: conwayBuffer,
               texture: textureBuffer,
            };
        },
        CLEAR(gl, _thisArg) {
            if(typeof _thisArg === 'undefined') throw new Error("You forgot _thisArg!");
            gl.deleteProgram(_thisArg.shaderProgram);
            _thisArg.atPos1 = undefined;
            //_thisArg.atPos2 = undefined;
            _thisArg.buffers = undefined;
        },
    },
    TEST: {
        DRAW(gl, _thisArg) {    //https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Adding_2D_content_to_a_WebGL_context
            if(typeof _thisArg === 'undefined') throw new Error("You forgot _thisArg!");
            const vertices = [
                -0.5, -0.5, 0.0,
                 0.5, -0.5, 0.0,
                 0.0,  0.5, 0.0
            ];
            gl.clearColor(0.0,0.0,0.0,1.0);
            gl.clearDepth(1.0);
            gl.enable(gl.DEPTH_TEST);
            gl.depthFunc(gl.LEQUAL);
            gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
            gl.bindBuffer(gl.ARRAY_BUFFER, _thisArg.buffers.position);
            const numComponents = 3;  // pull out 3 values per iteration
            const type = gl.FLOAT;    // the data in the buffer is 32bit floats
            const normalize = false;  // don't normalize
            const stride = 0;         // how many bytes to get from one set of values to the next
                                      // 0 = use type and numComponents above
            const offset = 0;         // how many bytes inside the buffer to start from
            gl.vertexAttribPointer(
                _thisArg.atPos1,
                numComponents,
                type,
                normalize,
                stride,
                offset);
            gl.enableVertexAttribArray(_thisArg.atPos1);
            gl.useProgram(_thisArg.shaderProgram);
            gl.uniform1f(_thisArg.unPos1, Math.floor(_thisArg.netTime) / 1000);
            //console.log(this.netTime);
            const offset2 = 0;
            const vertexCount = 3;
            gl.drawArrays(gl.TRIANGLES, offset2, vertexCount);
        },
        SETUP(gl, _thisArg) {   
            const vertices = [
                -0.5, -0.5, 0,
                 0.5, -0.5, 0,
                 0.0,  0.6, 0,
            ];
            
            if(typeof _thisArg === 'undefined') throw new Error("You forgot _thisArg!");
            const fragmentShader = loadFile("./shaders/simple.frag");
            const vertexShader = loadFile("./shaders/simple.vert");
            _thisArg.shaderProgram = _thisArg._createSimpleShader(_thisArg._gl, vertexShader, fragmentShader);            
            _thisArg.atPos1 = gl.getAttribLocation(_thisArg.shaderProgram, 'aVertexPosition');
            _thisArg.unPos1 = gl.getUniformLocation(_thisArg.shaderProgram, 'timeVal');
            const positionBuffer = gl.createBuffer();
            gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
            gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
            _thisArg.buffers = {position: positionBuffer};
            
        },
        CLEAR(gl, _thisArg) {
            if(typeof _thisArg === 'undefined') throw new Error("You forgot _thisArg!");
            gl.deleteProgram(_thisArg.shaderProgram);
            _thisArg.atPos1 = undefined;
            _thisArg.unPos1 = undefined;
            _thisArg.buffers = undefined;
        },
    },
}




class ConwayDrawer {
    constructor(sizeX, sizeY, gridType, rangeX, rangeY) {
        this.gridType = gridType;
        this.maxX = sizeX;
        this.posX = 0;
        this.rangeX = 10;
        this.maxY = sizeY;
        this.posY = 0;
        this.rangeY = 10;
        this.netTime = 0;
        this._maskDraw = false;
        this._setupGL();
        this.gridType.SETUP(this._gl, this);
    }
    moveWindow(offX, offY) {
        this.posX += offX;
        this.posY += offY;
    }
    scaleWindow(sFac) {
        this.rangeX = sFac;
        this.rangeY = sFac;
    }
    swapGridType(gridType) {
        this._maskDraw = true;
        this.gridType.CLEAR(this._gl, this);
        this.gridType = gridType;
        this.gridType.SETUP(this._gl, this);
        this._maskDraw = false;
    }

    _copy4ArraysTo1(arr1, arr2, arr3, arr4) {
        let retArray = [...Array(rangeX)].map(e => Array(rangeY));
        const maxX = this.maxX;
        const maxY = this.maxY;
        const rangeX = this.rangeX;
        const rangeY = this.rangeY;
        const posX = this.posX;
        const posY = this.posY;
        for(let x = 0; x < rangeX; x++) {
            for(let y = 0; y < rangeY; y++) {
                if(y > (maxY - posY) ) {
                    if(x > (maxX - posX) ) {
                        retArray[x][y] = arr4[x - maxX + posX][y - maxY + posY];
                    } else {
                        retArray[x][y] = arr2[x][y - maxY + posY];
                    }
                } else {
                    if(x > (maxX - posX) ) {
                        retArray[x][y] = arr3[x - maxX + posX][y];
                    } else {
                        retArray[x][y] = arr1[x][y];
                    }
                }
            }
        }
        return retArray.flat();
    }

    getTiles() {
        const maxX = this.maxX;
        const maxY = this.maxY;
        const rangeX = this.rangeX;
        const rangeY = this.rangeY;
        const posX = this.posX;
        const posY = this.posY;
        if(posX + rangeX > maxX) {
            if(posY + rangeY > maxY) {
                let arr1 = requestTiles(posX, posY,                   maxX,                   maxY);
                let arr2 = requestTiles(posX,    0,                   maxX, (posY + rangeY) % maxY);
                let arr3 = requestTiles(   0, posY, (posX + rangeX) % maxX,                   maxY);
                let arr4 = requestTiles(   0,    0, (posX + rangeX) % maxX, (posY + rangeY) % maxY);
                return this._copy4ArraysTo1(arr1,arr2,arr3,arr4);
            } else {
                let arr1 = requestTiles(posX, posY,                   maxX,          posY + rangeY);
                let arr2 = requestTiles(   0, posY, (posX + rangeX) % maxX,          posY + rangeY);
                return this._copy4ArraysTo1(arr1,null,arr2,null);
            }
        } else {
            if(posY + rangeY > maxY) {
                let arr1 = requestTiles(posX, posY,          posX + rangeX,                   maxY);
                let arr2 = requestTiles(posX,    0,          posX + rangeX, (posY + rangeY) % maxY);
                return this._copy4ArraysTo1(arr1,arr2,null,null);
            } else {
                return requestTiles(posX, posY,          posX + rangeX,          posX + rangeX);
            }
        }
    }

    _setupGL() {     //https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Getting_started_with_WebGL
        this._canvas = document.querySelector("#glCanvas");
        this._gl = this._canvas.getContext("webgl");
        if(this._gl === null) {
            alert("Unable to init WebGL.");
            return;
        }
        this._gl.clearColor(0.0, 0.0, 0.0, 1.0);
        this._gl.clear(this._gl.COLOR_BUFFER_BIT);
    }

    draw(deltaTime) {
        if(this._maskDraw) return;
        this.netTime += deltaTime;
        this.gridType.DRAW(this._gl, this);
        //requestAnimationFrame(()=> this.draw());
    }

    _loadShader(gl, type, source) {     //https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Adding_2D_content_to_a_WebGL_context
        const shader = gl.createShader(type);
        gl.shaderSource(shader, source);
        gl.compileShader(shader);
        if( !gl.getShaderParameter(shader, gl.COMPILE_STATUS) ) {
            alert("An error occurred compiling the shaders: " + gl.getShaderInfoLog(shader));
            gl.deleteShader(shader);
            return null;
        }
        return shader;
    }

    _createSimpleShader(gl, vertexSource, fragmentSource) {     //https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Adding_2D_content_to_a_WebGL_context
        const vertexShader = this._loadShader(gl, gl.VERTEX_SHADER, vertexSource);
        const fragmentShader = this._loadShader(gl, gl.FRAGMENT_SHADER, fragmentSource);

        const shaderProgram = gl.createProgram();
        gl.attachShader(shaderProgram, vertexShader);
        gl.attachShader(shaderProgram, fragmentShader);
        gl.linkProgram(shaderProgram);

        if( !gl.getProgramParameter(shaderProgram, gl.LINK_STATUS) ) {
            alert("Unable to initialize the shader program: " + gl.getProgramInfoLog(shaderProgram) );
            return null;
        }
        
        return shaderProgram;
    }
}


