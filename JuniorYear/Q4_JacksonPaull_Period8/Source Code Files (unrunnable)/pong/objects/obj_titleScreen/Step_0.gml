if(keyboard_check_pressed(vk_up))
{
	buttonOn--;	
}
if(keyboard_check_pressed(vk_down))
{
	buttonOn++;	
}

if(buttonOn<0)
	buttonOn = array_length_1d(buttonNames)-1;

if(buttonOn>(array_length_1d(buttonNames)-1))
	buttonOn = 0;
	


if(keyboard_check_pressed(vk_enter)&&released)
{
	switch(buttonOn)
	{
		case 0: room_goto_next(); break;
		case 1: game_end();
	}
	released = false;
}
if(keyboard_check_released(vk_enter))
{
	released = true;	
}