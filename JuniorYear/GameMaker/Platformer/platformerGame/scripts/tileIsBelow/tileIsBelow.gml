var tile = argument0;

var t1 = tilemap_get_at_pixel(tilemap,bbox_left,bbox_bottom+1);
var t2 = tilemap_get_at_pixel(tilemap,bbox_right,bbox_bottom+1);

if((tile_get_index(t1)==tile) || (tile_get_index(t2)==tile))
{		
	return true;
}
return false;