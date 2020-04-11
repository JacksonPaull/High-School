processPlayerMovement();


if(!gcd){
	if (keyboard_check(ord("F")))
	{
		state = playerstate.attack1;
	}
	if (keyboard_check(ord("G")))
	{
		state = playerstate.attackFireball;
	}
}