switch(state)
{
	case playerstate.idle: 
		state_idle();
		break;
	case playerstate.jumping:
		state_jumping();
		break;
	case playerstate.stunned:
		break;
	case playerstate.falling:
		state_falling();
		break;
}

if(canMove)
	process_movement();