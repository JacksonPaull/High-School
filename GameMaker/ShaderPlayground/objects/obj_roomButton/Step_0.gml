if(global.UI_active)
{
	var clicked = false
	if(point_in_rectangle(mouse_x,
							mouse_y,x-sprite_get_width(sprite_index)/2,
							y-sprite_get_height(sprite_index)/2,
							x+sprite_get_width(sprite_index)/2,
							y+sprite_get_height(sprite_index)/2) 
				and 
				mouse_check_button_pressed(mb_left))
		clicked = true
	
	switch(movedir)
	{
		case "forward": 
			if(keyboard_check_pressed(vk_right) or clicked)
				if(room_exists(room_next(room)))
					room_goto_next()
				else	
					room_goto(room_first)
		break;
		
		case "backward":
			if(keyboard_check_pressed(vk_left) or clicked)
				if(room_exists(room_previous(room)))
					room_goto_previous()
				else
					room_goto(room_last)
		break;
	}
}