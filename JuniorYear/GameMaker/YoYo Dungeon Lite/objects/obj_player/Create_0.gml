/*
INITIALIZE ALL VARIABLES FOR THE PLAYER
*/

//Attack Variables
state = playerstate.idle;
endAnimation = false;
hitByAttack = ds_list_create();
firstTime = true;
nextState = "idle";
alarm[1] = 0; //GLOBAL COOLDOWN
gcd = false;
//Animation
animationSpeed=0.5;
dir=DIR_STOP;
image_index=0;

//Movement
playerspeed=5;

//collisions
var l = layer_get_id("collisions");
tilemap= layer_tilemap_get_id(l);

//sprite info
sprite_bbox_left = sprite_get_bbox_left(sprite_index) - sprite_get_xoffset(sprite_index);
sprite_bbox_right = sprite_get_bbox_right(sprite_index) - sprite_get_xoffset(sprite_index);
sprite_bbox_top = sprite_get_bbox_top(sprite_index) - sprite_get_yoffset(sprite_index);
sprite_bbox_bottom = sprite_get_bbox_bottom(sprite_index) - sprite_get_yoffset(sprite_index);