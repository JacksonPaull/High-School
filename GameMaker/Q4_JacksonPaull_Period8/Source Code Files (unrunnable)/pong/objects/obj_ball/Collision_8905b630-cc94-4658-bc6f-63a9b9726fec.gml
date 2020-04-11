switch(movingDirection)
{
	case DIR_LEFT: movingDirection = DIR_RIGHT;	break;
	case DIR_RIGHT: movingDirection = DIR_LEFT;	break;
}
with(other)
{
	if(playerNum == 0)
	{
		with(obj_score)
		{
			lastHitBy = 0;	
		}
	}
	else if(playerNum == 1)
	{
		with(obj_score)
		{
			lastHitBy = 1;	
		}
	}
}
dy = floor(random_range(-5,6));