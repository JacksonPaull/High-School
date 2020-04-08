///@param length
var currentTime = argument0
var time = shader_get_uniform(shdr_hitShader,"time")


draw_self()
shader_set(shdr_hitShader)
shader_set_uniform_f(time,(currentTime/60))

draw_self()
shader_reset()