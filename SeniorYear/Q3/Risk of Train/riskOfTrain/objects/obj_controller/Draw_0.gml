draw_sprite(spr_button_cross,0,100,100)
draw_sprite(spr_button_noCross,0,700,100)

if(alarm[0]>0)
{
	draw_sprite_ext(spr_thonking,0,obj_player.x,obj_player.y-sprite_get_height(spr_player),0.05,0.05,0,c_white,1)
}