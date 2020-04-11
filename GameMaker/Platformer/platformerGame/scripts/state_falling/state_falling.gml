//process downward collisions and horizontal collisions until hit
if(!tileIsBelow(TILE_GROUND))
{
	y+=1;
}
else
{
	nextState = playerstate.idle;
}