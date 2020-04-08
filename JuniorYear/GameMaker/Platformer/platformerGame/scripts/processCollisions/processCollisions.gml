var t1 = tilemap_get_at_pixel(tilemap,bbox_left,bbox_bottom) & tile_index_mask;
var t2 = tilemap_get_at_pixel(tilemap,bbox_right,bbox_bottom) & tile_index_mask;
	
//if there is a collision tile at all - CHANGE THIS FOR SPECIALIZED COLLISIONS LATER
if((tile_get_index(t1)==TILE_GROUND) || (tile_get_index(t2)==TILE_GROUND))
{		
	y=((bbox_bottom & ~31)-1) - sprite_bbox_bottom;	
}