/// movePlayer
// You can write your code in this editor

//Process movement
if(keyboard_check(vk_right) or keyboard_check(ord("D"))){
	x+=4;
}
if(keyboard_check(vk_left) or keyboard_check(ord("A"))){
	x-=4;
}
if(keyboard_check(vk_up) or keyboard_check(ord("W"))){
	y-=4;
}
if(keyboard_check(vk_down) or keyboard_check(ord("S"))){
	y+=4;
}

//Set player to face mouse
image_angle = point_direction(x,y,mouse_x,mouse_y);

//handle firing
if(mouse_check_button(mb_left) and cooldown<1){
	
	instance_create_layer(x,y,"layer_bullet",obj_playerBullet);
	cooldown = 5;
}
cooldown-=1;

//handle death
if(hp<=0)
{
	var cx = camera_get_view_x(view_camera[0]);
	var cy = camera_get_view_y(view_camera[0]);
	var cw = camera_get_view_width(view_camera[0]);
	instance_create_layer(cx+(cw/2),cy+room_height/2,"Instances",obj_deathTitle,)
}