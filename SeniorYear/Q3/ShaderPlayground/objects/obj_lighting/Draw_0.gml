if !surface_exists(surf)
{
	
	//create surface to match camera
	var _cw = camera_get_view_width(view_camera[0])
	var _ch = camera_get_view_height(view_camera[0])
	surf = surface_create(_cw,_ch)
	
	draw_set_color(c_black)
	draw_set_alpha(0.8)
	draw_rectangle(0,0,room_width,room_height,false)
	
	//draw dark overlay on surface
	surface_set_target(surf)
	draw_set_color(c_black)
	draw_set_alpha(0.8)
	draw_rectangle(0,0,_cw,_ch,false)
	
	surface_reset_target()
}

else //surface exists
{
	var _cw = camera_get_view_width(view_camera[0])
	var _ch = camera_get_view_height(view_camera[0])
	var _cx = camera_get_view_x(view_camera[0])
	var _cy = camera_get_view_y(view_camera[0])
	surface_set_target(surf)
	
	draw_set_color(c_black)
	draw_set_alpha(0.8)
	draw_rectangle(0,0,_cw,_ch,0)
	gpu_set_blendmode(bm_subtract)
	
	with(obj_lightParent)
	{
		//only light instance rn is the torch, add a switch case later
		switch(object_index)
		{
			case obj_torch:
				draw_sprite_ext(spr_torchGlow2,0,x-_cx,y-_cy,0.2,0.2,0,c_white,1)
		
				gpu_set_blendmode(bm_add)
				draw_sprite_ext(spr_torchGlow2,0,x-_cx,y-_cy,0.2,0.2,0,c_orange,0.3)
				
				gpu_set_blendmode(bm_subtract)
			break;
		}
	}
	
	
	gpu_set_blendmode(bm_normal)
	draw_set_alpha(1)

	surface_reset_target()
	draw_surface(surf,_cx,_cy)
}