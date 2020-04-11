///@param alpha
var alpha = argument0

var sh_alpha = shader_get_uniform(shdr_borderShader,"alpha")

shader_set(shdr_borderShader)
shader_set_uniform_f(sh_alpha, alpha)
draw_self()
shader_reset()