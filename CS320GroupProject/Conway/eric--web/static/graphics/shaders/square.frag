precision mediump float;

varying vec2 v_texcoord;

uniform sampler2D u_texture;
varying float tVal;

void main() {
    gl_FragColor = texture2D(u_texture, 1.0 * v_texcoord);
    //gl_FragColor = texture2D(u_texture, vec2(1.0,1.0));
    //gl_FragColor = vec4(1.0, 0.5, 0.2, 1.0);
}
