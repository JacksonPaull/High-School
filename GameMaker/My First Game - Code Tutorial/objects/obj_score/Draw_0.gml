/// @description Insert description here
// You can write your code in this editor

//get camera dimensions
var cx = camera_get_view_x(view_camera[0]);
var cy = camera_get_view_y(view_camera[0]);
var cw = camera_get_view_width(view_camera[0]);

//set style
draw_set_font(fnt_score);
draw_set_color(c_white);

//draw score
draw_text(cx + (cw / 2), cy + 25, string(theScore));
draw_text(cx+20,cy+camera_get_view_height(view_camera[0])-80,"Lives");

//draw lives
with(obj_player){
	for(var i=0;i<hp;i++)
	{
		draw_sprite(spr_heart,0,cx + 64*i, cy+camera_get_view_height(view_camera[0]));
	}
}