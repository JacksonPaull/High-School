///@param sprite
///@param x
///@param y
///@param scale
///@param alpha


var sprite = argument0
var _x = argument1
var _y = argument2
var scale = argument3
var alpha = argument4



var upixelH = shader_get_uniform(shdr_borderShader,"pixelH");
var upixelW = shader_get_uniform(shdr_borderShader,"pixelW");
var texelW = texture_get_texel_width(sprite_get_texture(sprite,0));
var texelH = texture_get_texel_height(sprite_get_texture(sprite,0));


shader_set(shdr_borderShader)
shader_set_uniform_f(upixelW,texelW)
shader_set_uniform_f(upixelH,texelH)
draw_sprite_ext(sprite,0,_x,_y,scale,scale,0,c_white,alpha)
shader_reset()