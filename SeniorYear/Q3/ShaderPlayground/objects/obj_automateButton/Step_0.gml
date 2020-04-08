var clicked = (point_in_rectangle(mouse_x,mouse_y,x-sprite_width/2,y-sprite_height/2,x+sprite_width/2,y+sprite_height/2) && mouse_check_button_pressed(mb_left))
//toggle bounce

if(clicked)
{
	bounce ^= true
	image_index = bounce
	if(bounce)
	{
		slider.mode = "bounce"	
	}
	
	else
	{
		slider.mode = "loop"
	}
}

