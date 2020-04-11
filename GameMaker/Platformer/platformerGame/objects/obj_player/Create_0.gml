//Movement scripts
state = playerstate.idle;
controller = -1;
canMove = true;
nextState = playerstate.idle;

//Collisions
sprite_bbox_left = sprite_get_bbox_left(sprite_index) - sprite_get_xoffset(sprite_index);
sprite_bbox_right = sprite_get_bbox_right(sprite_index) - sprite_get_xoffset(sprite_index);
sprite_bbox_top = sprite_get_bbox_top(sprite_index) - sprite_get_yoffset(sprite_index);
sprite_bbox_bottom = sprite_get_bbox_bottom(sprite_index) - sprite_get_yoffset(sprite_index);

var l = layer_get_id("layer_ground");
tilemap= layer_tilemap_get_id(l);