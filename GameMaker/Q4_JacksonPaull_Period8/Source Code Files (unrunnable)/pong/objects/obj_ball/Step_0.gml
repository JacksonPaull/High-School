if(movingDirection = DIR_LEFT)
	x-=BALL_SPEED;
else if(movingDirection = DIR_RIGHT)
	x+=BALL_SPEED;
	


y+=dy;
processBallCollisions();