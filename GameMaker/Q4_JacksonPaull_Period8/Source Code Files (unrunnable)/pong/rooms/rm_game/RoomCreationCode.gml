layer_set_visible("layer_collisions", false)
with(obj_score)
{
	resetGame();
	waiting = true;
}
instance_create_layer(512,384,layer_get_id("layer_instances"),ball_spawn);