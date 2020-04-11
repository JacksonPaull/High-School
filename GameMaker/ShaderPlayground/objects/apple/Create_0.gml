image_speed = 0

currentTime = 0

upixelH = shader_get_uniform(shdr_borderShader,"pixelH");
upixelW = shader_get_uniform(shdr_borderShader,"pixelW");
texelW = texture_get_texel_width(sprite_get_texture(sprite_index,0));
texelH = texture_get_texel_height(sprite_get_texture(sprite_index,0));