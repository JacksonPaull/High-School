//moving right
if(movingDirection = DIR_RIGHT)
{
	var t2 = tilemap_get_at_pixel(map,x+5,y) & tile_index_mask;

	if(tile_get_index(t2) == TILE_WALL)
	{
		movingDirection=DIR_LEFT;
	}
	if(tile_get_index(t2) == TILE_GOAL)
	{
		with(obj_score)
		{
			scoreIncrease(lastHitBy);
			resetGame();
			waiting = true;
		}
		instance_create_layer(512,384,layer_get_id("layer_instances"),ball_spawn);
		instance_destroy();
		
		
	}
}

//moving left
else if(movingDirection = DIR_LEFT)
{
	var t2 = tilemap_get_at_pixel(map,x-5,y) & tile_index_mask;	

	if(tile_get_index(t2) == TILE_WALL)
	{
		movingDirection=DIR_RIGHT;
	}
	if(tile_get_index(t2) == TILE_GOAL)
	{
		with(obj_score)
		{
			scoreIncrease(lastHitBy);
			resetGame();
			waiting = true;
		}
		instance_destroy();
		instance_create_layer(512,384,layer_get_id("layer_instances"),ball_spawn);		
		
	}
	
}

//moving up
if(dy<=0)
{
	var t1 = tilemap_get_at_pixel(map,x,y-5) & tile_index_mask;
	
	if(tile_get_index(t1) == TILE_WALL)
	{
		dy*=-1;	
	}

}

//moving down
else if(dy>=0)
{	
	var t1 = tilemap_get_at_pixel(map,x,y+5) & tile_index_mask;
		
	if(tile_get_index(t1) == TILE_WALL)
	{
		dy*=-1;	
	}

	return;
}