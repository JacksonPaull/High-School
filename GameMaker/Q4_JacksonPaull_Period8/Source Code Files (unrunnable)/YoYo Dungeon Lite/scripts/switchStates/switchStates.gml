switch(nextState)
{	
	case "attack2":
		state = playerstate.attack2;
		firstTime = true;
		break;
		
	case "idle":
		image_index = sBlue_Standing;
		image_speed = 1;
		firstTime = true;
		globalCooldown(10);
		state = playerstate.idle; 
		mask_index = sBlue_Standing;
	break;
	
}
