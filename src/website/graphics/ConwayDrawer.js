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


class ConwayDrawer {
    constructor(sizeX, sizeY, gridType) {
        this.gridType = gridType;
        this.maxX = sizeX;
        this.posX = 0;
        this.maxY = sizeY;
        this.posY = 0;
        this.netTime = 0;
        this._setupGL();
        let fragmentShader = loadFile("./shaders/simple.frag");
        let vertexShader = loadFile("./shaders/simple.vert");
        this.shaderProgram = this._createSimpleShader(this._gl, vertexShader, fragmentShader);
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
        this.netTime += deltaTime;
        let gl = this._gl;
        this._testDraw(gl);
        //requestAnimationFrame(()=> this.draw());
    }
    _testDraw(gl) {   //https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial/Adding_2D_content_to_a_WebGL_context
        let vertices = [
            -0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0
        ];
        const positionBuffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
        let buffers = {position: positionBuffer};
        gl.clearColor(0.0,0.0,0.0,1.0);
        gl.clearDepth(1.0);
        gl.enable(gl.DEPTH_TEST);
        gl.depthFunc(gl.LEQUAL);
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
        gl.bindBuffer(gl.ARRAY_BUFFER, buffers.position);
        const atPos1 = gl.getAttribLocation(this.shaderProgram, 'aVertexPosition');
        const unPos1 = gl.getUniformLocation(this.shaderProgram, 'timeVal');
        const numComponents = 3;  // pull out 3 values per iteration
        const type = gl.FLOAT;    // the data in the buffer is 32bit floats
        const normalize = false;  // don't normalize
        const stride = 0;         // how many bytes to get from one set of values to the next
                                  // 0 = use type and numComponents above
        const offset = 0;         // how many bytes inside the buffer to start from
        gl.vertexAttribPointer(
            atPos1,
            numComponents,
            type,
            normalize,
            stride,
            offset);
        gl.enableVertexAttribArray(atPos1);
        gl.useProgram(this.shaderProgram);
        gl.uniform1f(unPos1, Math.floor(this.netTime) / 1000);
        console.log(this.netTime);
        const offset2 = 0;
        const vertexCount = 3;
        gl.drawArrays(gl.TRIANGLES, offset2, vertexCount);
        
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


