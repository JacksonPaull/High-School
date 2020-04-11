canMove = true;
process_input();
if(!tileIsBelow(TILE_GROUND))
	nextState = playerstate.falling;