attribute vec4 aVertexPosition;

varying vec2 v_texcoord;
//https://webglfundamentals.org/webgl/lessons/webgl-3d-textures.html

uniform float deltaT;
varying float tVal;

void main() {
    gl_Position = aVertexPosition;
    tVal = deltaT;
    v_texcoord = aVertexPosition.xy * 0.5 + vec2(0.5,0.5);
}