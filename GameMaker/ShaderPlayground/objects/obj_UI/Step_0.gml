if(current_time >0.001 and current_time <1000)
{
	with(obj_UI)
	{
		persistent = true
	}
}


if(keyboard_check_pressed(vk_tab))
{
	global.UI_active ^= true
	with(obj_UI)
		visible ^= true
}

//Need to add checks for moues, that checks if it clicks any shaders, set them to active. esc resets?
