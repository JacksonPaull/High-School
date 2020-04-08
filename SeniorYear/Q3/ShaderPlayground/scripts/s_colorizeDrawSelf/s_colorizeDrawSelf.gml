///@param r
///@param g
///@param b

var r = argument0
var g = argument1
var b = argument2

var red = shader_get_uniform(shdr_colorize, "red")
var blue = shader_get_uniform(shdr_colorize, "blue")
var green = shader_get_uniform(shdr_colorize, "green")

shader_set(shdr_colorize)
shader_set_uniform_f(red,r)
shader_set_uniform_f(green,g)
shader_set_uniform_f(blue,b)
draw_self()

shader_reset()
