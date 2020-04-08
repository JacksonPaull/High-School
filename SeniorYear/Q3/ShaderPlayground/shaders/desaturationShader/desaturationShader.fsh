//
// Simple passthrough fragment shader
//
varying vec2 v_vTexcoord;
varying vec4 v_vColour;

uniform float strength;

void main()
{
	vec4 base_col = v_vColour * texture2D( gm_BaseTexture, v_vTexcoord );
	float value = dot(base_col.rgb, vec3(0.299,0.587,0.144));
	vec3 out_col = mix(base_col.rgb, vec3(value), strength);
    gl_FragColor = v_vColour * vec4(out_col,base_col.a);
}
