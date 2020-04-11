///@param alpha


var a = argument0


var alpha = shader_get_uniform(shdr_alpha,"alpha")
shader_set(shdr_alpha)
shader_set_uniform_f(alpha,a)

draw_self()

shader_reset()