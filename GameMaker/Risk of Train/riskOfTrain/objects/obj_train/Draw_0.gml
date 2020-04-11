draw_sprite_ext(sprite_index,0,x,y,2,2,0,c_white,1)

if(death)
{
	draw_sprite_ext(spr_death,0,room_width/2,room_height/2,0.8,1,0,c_white,time)
	draw_set_alpha(time)
	draw_text(room_width/2-string_length("Press escape to try again")*5,7*room_height/10,"Press escape to try again")
	draw_set_alpha(1)
	time+=0.01
}

if(crossed)
{
	draw_set_alpha(time)
	draw_sprite(spr_thumbsUp,0,room_width/2,room_height/2)
	draw_set_halign(fa_center)
	draw_set_valign(fa_top)
	draw_set_font(fnt_font)
	draw_text(room_width/2,7*room_height/10, "You win wahoo.\n Press escape to try again")
	time+=0.01
	draw_set_alpha(1)
}