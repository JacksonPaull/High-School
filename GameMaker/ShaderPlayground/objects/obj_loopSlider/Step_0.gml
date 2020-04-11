#macro SLIDERSPEED global.sliderspeed


//Process clicks
if(global.UI_active)
{
		
	if(point_in_rectangle(mouse_x, mouse_y,
							x-sprite_get_width(sprite_index)*1.5/2,
							y-sprite_get_height(sprite_index)*1.5/2,
							x+sprite_get_width(sprite_index)*1.5/2,
							y+sprite_get_height(sprite_index)*1.5/2))
	{ 
		//Mouse is hovering
		//image_index = 1 //set to hover sprite
		if(mouse_check_button_pressed(mb_left))
		{
			//Mouse is clicked
			on ^= true
			image_index = on*2
		}
	}
	else
		image_index = on*2
	
}
if(on)
{
	switch(mode)
	{
		case "bounce":
			slider.x += dir*SLIDERSPEED
			if(slider.x >= slider.xstart+slideWidth)
			{
				dir = -1
			}
			else if(slider.x <= slider.xstart-slideWidth)
			{
				dir = 1
			}
		break;
		
		case "loop":
			slider.x += SLIDERSPEED
			if(slider.x >= slider.xstart+slideWidth)
			{
				slider.x = slider.xstart-slideWidth
			}
		break;
	}
	
}
	

