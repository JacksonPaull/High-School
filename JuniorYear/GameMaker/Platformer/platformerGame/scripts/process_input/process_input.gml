if(gamepad_button_check(controller,gp_face2) || keyboard_check_pressed(vk_space))
{
	nextState = playerstate.jumping;
	alarm[0] = 30;
}