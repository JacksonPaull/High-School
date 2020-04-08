//obj_player.y = 320;

counter++;
//waited 0 seconds
if(counter<30)
	shouldDisplay = 3;


//waited 1 second
else if(counter<60)
	shouldDisplay = 2;

//waited 2 seconds
else if(counter<90)
	shouldDisplay = 1;

//waited 3 seconds
else
{
	instance_create_layer(512,384,layer_get_id("layer_instances"),obj_ball)
	with(obj_score)
	{
		lastHitBy = -1;	
	}
	counter = 0;
	waiting = false;
	with(ball_spawn)
	instance_destroy();
}