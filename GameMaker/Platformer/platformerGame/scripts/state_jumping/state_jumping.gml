canMove=true;

if(gamepad_button_check_released(controller,gp_face2) || keyboard_check_released(vk_space))
{
	nextState = playerstate.falling;
}
else
{
	y-=5
}