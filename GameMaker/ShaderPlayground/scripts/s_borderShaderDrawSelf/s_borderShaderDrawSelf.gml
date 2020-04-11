var upixelH = shader_get_uniform(shdr_borderShader,"pixelH");
var upixelW = shader_get_uniform(shdr_borderShader,"pixelW");
var texelW = texture_get_texel_width(sprite_get_texture(sprite_index,0));
var texelH = texture_get_texel_height(sprite_get_texture(sprite_index,0));


shader_set(shdr_borderShader)
shader_set_uniform_f(upixelW,texelW)
shader_set_uniform_f(upixelH,texelH)
draw_self()
shader_reset()