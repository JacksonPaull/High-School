//determine the mouse position and clicking status

if(global.UI_active)
{
	
	if( point_in_rectangle(mouse_x,
							mouse_y,
							x-sprite_get_width(sprite_index)*1.5/2,
							y-sprite_get_height(sprite_index)*1.5/2,
							x+sprite_get_width(sprite_index)*1.5/2,
							y+sprite_get_height(sprite_index)*1.5/2) 
					and 
							mouse_check_button_pressed(mb_left))
		hovering = true
		
	if(hovering)
	{
	//Mouse is hovering over this slider and clicking this slider
		var diff = mouse_x-x // distance to mouse
		move_rate = lerp(diff, move_rate, inertia)-0.5*move_rate
		x+=move_rate
	}
}
if(mouse_check_button_released(mb_left))
	hovering = false
	


x = clamp(x,xstart-slideWidth ,xstart+slideWidth)
switch(slidevar)
{
	case 1: global.slider1 = ((x-xstart)/slideWidth+1)/2.00
			break;
	case 2: global.slider2 = ((x-xstart)/slideWidth+1)/2.00
			break;
	case 3: global.slider3 = ((x-xstart)/slideWidth+1)/2.00
			break;
	case 4: global.sliderspeed = ((x-xstart)/slideWidth+1)/2.00*5
			break;
	case -1: show_debug_message("not instantiated")
			break;
	default: show_debug_overlay(true) 
			 show_debug_message("What the fuck?")
}	
