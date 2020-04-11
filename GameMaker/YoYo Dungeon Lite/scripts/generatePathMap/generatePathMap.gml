var collisionLayer = layer_get_id("collisions");
var collisionMap = layer_tilemap_get_id(collisionLayer);
pathMap = [[]];
var objWidth = ceil(sprite_width / GRID_SIZE);
var objHeight = ceil(sprite_height / GRID_SIZE);


for(var r = 0; r<ceil(room_width/GRID_SIZE);r+=1)
{
	for(var c = 0; c<ceil(room_height/GRID_SIZE);c+=1)
	{
		var tile = tilemap_get_at_pixel(collisionMap,r*GRID_SIZE,c*GRID_SIZE);
		var tileIndex = tile_get_index(tile);
		var passable = true;
		for(var i =0;i<array_length_1d(collisionTiles);i++)
		{
			if(tileIndex == collisionTiles[i]) //If the tile is not passable by the object passable is set to false
			{
				passable = false;
			}
		}
		pathMap[r,c] = passable;
	}
}

for(var r = 0;r<array_length_1d(pathMap)-objHeight;r++)
{
	for(var c = 0;c<array_length_2d(pathMap,r)-objHeight;c++)
	{
		for(var i =0; i<objHeight;i++)
		{
			if(!pathMap[r+i,c+i])
			{
				pathMap[r,c]=false;
			}
		}
	}
}

for(var r = 0;r<array_length_1d(pathMap);r++)
{
	for(var c = array_length_2d(pathMap,r)-objWidth;c<array_length_2d(pathMap,r);c++)
	{	
		pathMap[r,c]=false;	
	}
}
for(var r = array_length_1d(pathMap)-objHeight;r<array_length_1d(pathMap);r++)
{
	for(var c = 0;c<array_length_2d(pathMap,r);c++)
	{	
		pathMap[r,c]=false;	
	}
}

