attribute vec4 aVertexPosition;
uniform float timeVal;


void main() {
    mat4 rotation = mat4( cos(timeVal), sin(timeVal), 0, 0,
                         -sin(timeVal), cos(timeVal), 0, 0,
                                     0,            0, 1, 0,
                                     0,            0, 0, 1);
    gl_Position = rotation * aVertexPosition;
}