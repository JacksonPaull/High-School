if(x>room_width+sprite_get_width(spr_trainBody))
	instance_destroy()
	

if(x > xstart+sprite_width*1.45) && first
{
	first = false
	with(obj_train)
	{
		needNewTrain = true
	}
}