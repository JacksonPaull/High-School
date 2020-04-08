//Processes collision for the player object, as no other objects should need collision checks


if(dir=DIR_DOWN){ //collide with all things down	
	var t1 = tilemap_get_at_pixel(tilemap,bbox_left,bbox_bottom) & tile_index_mask;
	var t2 = tilemap_get_at_pixel(tilemap,bbox_right,bbox_bottom) & tile_index_mask;
	
	//if there is a collision tile at all - CHANGE THIS FOR SPECIALIZED COLLISIONS LATER
	if((tile_get_index(t1)==TILE_BRICK) || (tile_get_index(t2)==TILE_BRICK)||(tile_get_index(t1)==TILE_WATER) || (tile_get_index(t2)==TILE_WATER))
	{		
		y=((bbox_bottom & ~63)-1) - sprite_bbox_bottom;		
	}
	
}
else if(dir=DIR_UP){//collide with all things up
	var t1 = tilemap_get_at_pixel(tilemap,bbox_left,bbox_top) & tile_index_mask;
	var t2 = tilemap_get_at_pixel(tilemap,bbox_right,bbox_top) & tile_index_mask;
	
	if((tile_get_index(t1)==TILE_BRICK) || (tile_get_index(t2)==TILE_BRICK)||(tile_get_index(t1)==TILE_WATER) || (tile_get_index(t2)==TILE_WATER))
	{
		y=((bbox_top+64)& ~63) - sprite_bbox_top+1;
	}
	
}
else if (dir=DIR_LEFT){
	var t1 = tilemap_get_at_pixel(tilemap,bbox_left,bbox_top) & tile_index_mask;
	var t2 = tilemap_get_at_pixel(tilemap,bbox_left,bbox_bottom) & tile_index_mask;
	
	if((tile_get_index(t1)==TILE_BRICK) || (tile_get_index(t2)==TILE_BRICK)||
	(tile_get_index(t1)==TILE_WATER) || (tile_get_index(t2)==TILE_WATER))
	{
		x=((bbox_left+64)& ~63)- sprite_bbox_left;
	}

}
else if(dir=DIR_RIGHT){
	var t1 = tilemap_get_at_pixel(tilemap,bbox_right,bbox_top) & tile_index_mask;
	var t2 = tilemap_get_at_pixel(tilemap,bbox_right,bbox_bottom) & tile_index_mask;
	
	if((tile_get_index(t1)==TILE_BRICK) || (tile_get_index(t2)==TILE_BRICK)||(tile_get_index(t1)==TILE_WATER) || (tile_get_index(t2)==TILE_WATER))
	{
		x=((bbox_right& ~63)-1) - sprite_bbox_right;
	}
}

