if(keyboard_check(ord("D")) || (gamepad_axis_value(controller,gp_axislh)>0))
{
	x+=5;
}
else if(keyboard_check(ord("A")) || (gamepad_axis_value(controller,gp_axislh)<0))
{
	x-=5;
}