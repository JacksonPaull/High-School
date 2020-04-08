if(train == -1)
{
	if(mouse_check_button_pressed(mb_left))
	{
		
		
		if(mouse_x>100 && mouse_x<100+sprite_get_width(spr_button_cross))
			if(mouse_y>100 and mouse_y<100+sprite_get_height(spr_button_cross))
			{
				//Mouse is intersecting with cross button
				train = determineTrain()
				show_debug_message("The value of train is: "+string(train))
				//Play animation of walking up
				if(obj_player.y>700)
				{
					obj_player.vspeed =-1
					crossing = true
				}			
			}
	
		if(mouse_x>700 && mouse_x<700+sprite_get_width(spr_button_noCross))
			if(mouse_y>100 and mouse_y<100+sprite_get_height(spr_button_noCross))
			{
				alarm[0] = 2 * room_speed
				//Mouse is intersecting with no cross button
				train = determineTrain()
				show_debug_message("The value of train is: "+string(train))
				if(train)
				{
					with(obj_train)
					{
						trainRunning = true
						hspeed = 45
					}
				}			
			}
	}
}

if(crossing && obj_player.vspeed = 0)
{
	crossing = false
	if(train)
	{
		with(obj_train)
		{
			trainRunning = true
			alarm[0] = 75
			hspeed = 45
		}
	}
	else
	{
		//Play animation of walking off
		show_debug_message("Player should disappear")
		obj_player.noTrain = true
		obj_train.alarm[1] = 90
		//Spawn you win thing and cut to bigass credits with me as the name for everything
	}
}

