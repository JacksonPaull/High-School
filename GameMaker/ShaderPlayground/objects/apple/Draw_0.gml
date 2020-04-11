shader_set(shdr_borderShader)
shader_set_uniform_f(upixelW,texelW)
shader_set_uniform_f(upixelH,texelH)
draw_self()
shader_reset()


if(currentTime>0)
{
	hit(currentTime)
	currentTime -=5
}


//============================
#region //DEBUG
if(global.debug)
{
	draw_text(5,room_height-20,current_time)
}
#endregion
//================================