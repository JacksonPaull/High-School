
switch(checkButtonsPressed())
{
	case "escape":
		global.pause = !global.pause
		if(global.pause)
		{
			menuIndex = 0;
			instance_deactivate_all(true)
		}
		else
			instance_activate_all()
	break;
	case "up": 
		if(indexChanged == false)
		{
			menuIndex -=1; 
			indexChanged = true; 
		}
	break;
	case "down":
		if(indexChanged == false)
		{
			menuIndex +=1; 
			indexChanged = true; 
		}
	break;
	case "enter":
	if(global.pause){
		switch(menuOptions[menuIndex])
		{
			case "Exit Game": game_end();break;	
			case "Resume": 
				global.pause = !global.pause
				instance_activate_all()
			break;
			case "Options": //create a submenu over this one that shows things like controller etc
				show_debug_message("Selected options");
			break;
		}
	break;
	}
}
	


if(menuIndex = -1)
	menuIndex = array_length_1d(menuOptions) -1
if(menuIndex = array_length_1d(menuOptions))
	menuIndex = 0
	
	

if(gamepad_axis_value(global.controller,gp_axislv)==0)
	indexChanged = false


show_debug_message(gamepad_axis_value(global.controller,gp_axislv))



/*
if(gamepad_button_check_pressed(global.controller,gp_padd))
	show_debug_message("Pad_d")
if(gamepad_button_check_pressed(global.controller,gp_padu))
	show_debug_message("Pad_u")
if(gamepad_button_check_pressed(global.controller,gp_padl))
	show_debug_message("Pad_l")
if(gamepad_button_check_pressed(global.controller,gp_padr))
	show_debug_message("Pad_r")
if(gamepad_button_check_pressed(global.controller,gp_face1))
	show_debug_message("Face 1")
if(gamepad_button_check_pressed(global.controller,gp_face2))
	show_debug_message("Face 2")
if(gamepad_button_check_pressed(global.controller,gp_face3))
	show_debug_message("Face 3")
if(gamepad_button_check_pressed(global.controller,gp_face4))
	show_debug_message("Face 4")
if(gamepad_button_check_pressed(global.controller,gp_shoulderl))
	show_debug_message("Pad_shoulerl")
if(gamepad_button_check_pressed(global.controller,gp_shoulderr))
	show_debug_message("Pad_shoulderr")
if(gamepad_button_check_pressed(global.controller,gp_shoulderrb))
	show_debug_message("Pad_shoulder rb")
if(gamepad_button_check_pressed(global.controller,gp_shoulderlb))
	show_debug_message("Pad_shoulder lb")
if(gamepad_button_check_pressed(global.controller,gp_start))
	show_debug_message("Pad_start")
if(gamepad_button_check_pressed(global.controller,gp_select))
	show_debug_message("Pad_select")
if(gamepad_button_check_pressed(global.controller,gp_stickl))
	show_debug_message("Pad_stickl")
if(gamepad_button_check_pressed(global.controller,gp_stickr))
	show_debug_message("Pad_stickr")














