//Check WASD and Arrow keys, then set movement accordingly
//and adjust animation accordingly
image_xscale=1;
if(keyboard_check(ord("W")) || keyboard_check(vk_up))
{
	y-=playerspeed;
	dir=DIR_UP;
	sprite_index=sBlue_Up;
}
else if(keyboard_check(ord("A")) || keyboard_check(vk_left))
{
	x-=playerspeed;
	dir=DIR_LEFT;
	sprite_index=sBlue_Left;
}
else 
if(keyboard_check(ord("S")) || keyboard_check(vk_down))
{
	
	y+=playerspeed;
	dir=DIR_DOWN;
	sprite_index=sBlue_Down;
}
else 
if(keyboard_check(ord("D")) || keyboard_check(vk_right))
{
	
	x+=playerspeed;
	dir=DIR_RIGHT;
	sprite_index=sBlue_Right;
}
else{
	if(dir=DIR_LEFT)
	{
		image_xscale=-1;
		sprite_index=sBlue_Standing;
	}
	else if(dir=DIR_RIGHT)
	{
		sprite_index=sBlue_Standing;
	}
	else if(dir=DIR_UP)
	{
		sprite_index=sBlue_Up;
		image_index=0;
		image_speed=0;
	}
	else if(dir=DIR_DOWN)
	{
		sprite_index=sBlue_Down;
		image_index=0;
		image_speed=0;
	}	
}

image_speed=animationSpeed;