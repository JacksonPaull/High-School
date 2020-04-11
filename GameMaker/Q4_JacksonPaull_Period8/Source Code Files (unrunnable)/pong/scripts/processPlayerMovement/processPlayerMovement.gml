var playerNum = argument0;

if(playerNum == 0)
{
	if(keyboard_check(ord("W")))
	{
		y-=PLAYER_SPEED;
	}
	if (keyboard_check(ord("S")))
	{
		y+=PLAYER_SPEED
	}
}
else if(playerNum == 1)
{
	if(keyboard_check(vk_up))
	{
		y-=PLAYER_SPEED;
	}
	if (keyboard_check(vk_down))
	{
		y+=PLAYER_SPEED
	}
}


//prevent players from moving out of bounds
if( y<=32)
	y=32;
if(y+128>=740)
	y=612;