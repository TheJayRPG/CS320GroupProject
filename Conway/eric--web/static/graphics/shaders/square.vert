attribute vec4 aVertexPosition;

varying vec2 v_texcoord;
//https://webglfundamentals.org/webgl/lessons/webgl-3d-textures.html


void main() {
    gl_Position = aVertexPosition;
    v_texcoord = aVertexPosition.xy * 0.5 + vec2(0.5,0.5);
}