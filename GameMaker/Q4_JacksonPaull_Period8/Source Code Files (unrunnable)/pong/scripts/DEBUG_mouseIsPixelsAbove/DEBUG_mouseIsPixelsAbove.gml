draw_set_font(fnt);
var map = layer_tilemap_get_id(layer_get_id("layer_collisions"))
for(var i =0;i<room_height;i++)
{
	var t1 = tile_get_index(tilemap_get_at_pixel(map,mouse_x,mouse_y+i));
	
	if(t1 == TILE_WALL)
	{
		for(var c =mouse_y;c>0;c--)
		{
			var t2 = tile_get_index(tilemap_get_at_pixel(map,mouse_x,c));
	
			if(t2 == TILE_WALL)
			{
				break;
			}
		}
		break;
	}
}


draw_text(200,200,"Mouse is "+string(i)+" pixels above a wall\nMouse is "+string(mouse_y-c)+" pixels below a wall");