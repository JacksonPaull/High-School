randomise();
movingDirection = round(random(1));
dy = floor(random_range(-5,6));
map = layer_tilemap_get_id(layer_get_id("layer_collisions"));
