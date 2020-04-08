///@param x1
///@param x2
///@param y

var x1 = argument0
var x2 = argument1
var y1 = argument2

var length = (x2-x1)-2*sprite_get_width(spr_sliderCap)

draw_sprite_ext(spr_sliderCap,0,x1,y1,1,1,0,c_white,1)
draw_sprite_ext(spr_sliderCenter,0,x1+sprite_get_width(spr_sliderCap),y1,length,1,0,c_white,1)
draw_sprite_ext(spr_sliderCap,0,x2,y1,-1,1,0,c_white,1)