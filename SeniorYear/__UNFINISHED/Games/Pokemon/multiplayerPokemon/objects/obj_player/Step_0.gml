switch(state)
{
	case playerstate.idle: processPlayerMovement(self); break;
	case playerstate.moving: show_debug_message("moving..."); break;
}

y += vsp;
x += hsp;