/// @description Insert description here
// You can write your code in this editor

image_alpha=0;
draw_set_color(c_red);
instance_destroy(obj_player);
instance_destroy(obj_controller);
instance_create_layer(camera_get_view_x(view_camera[0]),camera_get_view_y(view_camera[0]),"Instances",obj_shade);

