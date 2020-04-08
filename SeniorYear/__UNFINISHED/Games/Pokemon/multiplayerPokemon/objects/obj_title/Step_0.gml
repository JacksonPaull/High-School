switch(checkButtonsPressed())
{
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
		switch(menuOptions[menuIndex])
		{
			case "Exit Game": game_end();break;	
			case "Start": 
				room_goto_next();
			break;
			case "Pause": //create a submenu over this one that shows things like controller etc
				show_debug_message("Should pause")
				global.pause = !global.pause
				with(obj_pauseMenu){
					menuIndex = 0;
					instance_deactivate_all(true)
				}
			break;
		}
	break;
}

if(menuIndex = -1)
	menuIndex = array_length_1d(menuOptions) -1
if(menuIndex = array_length_1d(menuOptions))
	menuIndex = 0
	
if(gamepad_axis_value(global.controller,gp_axislv)==0)
	indexChanged = false