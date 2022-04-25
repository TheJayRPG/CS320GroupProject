precision mediump float;

varying vec2 v_texcoord;
varying float tVal;

uniform sampler2D u_texture;
uniform sampler2D p_texture;

void main() {
    float deltaT = tVal;
    vec4 p_color = texture2D(p_texture, 1.0 * v_texcoord);
    vec4 u_color = texture2D(u_texture, 1.0 * v_texcoord);
    //gl_FragColor = vec4(pow(deltaT*sqrt(float(p_color.r)) + (1.0-deltaT)*sqrt(float(u_color.r)),2.0),
    //                    pow(deltaT*sqrt(float(p_color.g)) + (1.0-deltaT)*sqrt(float(u_color.g)),2.0),
    //                    pow(deltaT*sqrt(float(p_color.b)) + (1.0-deltaT)*sqrt(float(u_color.b)),2.0),
    //                    pow(deltaT*sqrt(float(p_color.a)) + (1.0-deltaT)*sqrt(float(u_color.a)),2.0));

    gl_FragColor = vec4(p_color.r, u_color.g, 0.0, 1.0);
    //gl_FragColor = texture2D(u_texture, vec2(1.0,1.0));
    //gl_FragColor = vec4(1.0, 0.5, 0.2, 1.0);
}
