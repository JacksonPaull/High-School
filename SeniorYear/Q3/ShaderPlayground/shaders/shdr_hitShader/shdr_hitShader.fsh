//
// Simple passthrough fragment shader
//
varying vec2 v_vTexcoord;
varying vec4 v_vColour;

uniform float time;

void main()
{
	float alpha = texture2D(gm_BaseTexture, v_vTexcoord).a;
	if(alpha!=0.0)
	{
		gl_FragColor = vec4(1.0,1.0,1.0,time);
	}
    
}
