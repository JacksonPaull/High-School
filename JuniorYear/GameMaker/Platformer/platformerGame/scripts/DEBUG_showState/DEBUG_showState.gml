var stateString;
switch(state)
{
	case playerstate.idle: stateString = "idle"; break;
	case playerstate.jumping: stateString = "jumping"; break;
	case playerstate.falling: stateString = "falling"; break;
	case playerstate.stunned: stateString = "stunned"; break;
	
}

draw_text(32,172,"State - "+stateString);