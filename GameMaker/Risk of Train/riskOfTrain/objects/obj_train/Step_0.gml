if(needNewTrain && trainRunning)
{
	instance_create_layer(xstart,ystart,layer,obj_trainBody)
	needNewTrain = false
}

if(x>room_width+sprite_get_width(spr_trainBody)) //stops moving offscreen
	hspeed = 0
	
if(x>room_width/2-sprite_width and obj_player.y<600)
{
	obj_player.x = x+sprite_width
}

