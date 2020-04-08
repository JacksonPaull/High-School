/*
PROCESS ALL PLAYER INPUT
*/

//If the player's moves are on cooldown then they are forced into an idle state
if(gcd = true)
	state = playerstate.idle

switch(state)
{
	case playerstate.idle: playerstate_idle_scripts(); break;	
	case playerstate.attack1: playerstate_attack1(); break;
	case playerstate.attack2: playerstate_attack2(); break;
	case playerstate.attackFireball: playerstate_attackFireball(); break;
}

//Process collisions with specific tiles
processPlayerCollisions();


