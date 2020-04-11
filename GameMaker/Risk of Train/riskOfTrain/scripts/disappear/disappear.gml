///@param time

var time = argument0
var totalTime = argument1

draw_sprite_ext(sprite_index,0,x,y,time/totalTime,time/totalTime,0,c_white,1)
return time-1