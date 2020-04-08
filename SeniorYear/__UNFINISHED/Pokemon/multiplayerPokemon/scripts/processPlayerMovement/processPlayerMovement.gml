/// @param player
/// @description move the player
var player = argument0;
var moveDir = -1;

with(player)
{
	
	switch(checkButtonsPressed())
	{
		case "up": 
			moveDir = UP;
			break;
		case "left": 
			moveDir = LEFT
			break;
		case "down": 
			moveDir = DOWN
			break;
		case "right": 
			moveDir = RIGHT
			break;
	}
	
	/*
		CHECK FOR COLLISIONS IN MOVEMENT DIRECTIOn
	*/
	
	//Can move
	if(moveDir != -1)
	{
		state = playerstate.moving;
		switch(moveDir)
		{
			case UP:
				player.sprite_index = spr_player_walking_male_up;
				image_speed = PLAYER_IMAGE_SPEED
				vsp = -MOVESPEED;
				break;
			case DOWN:
				player.sprite_index = spr_player_walking_male_down;
				image_speed = PLAYER_IMAGE_SPEED
				vsp = MOVESPEED;
				break;
			case LEFT: 
				player.sprite_index = spr_player_walking_male_left;
				image_speed = PLAYER_IMAGE_SPEED
				hsp = -MOVESPEED;
				break;
			case RIGHT:
				player.sprite_index = spr_player_walking_male_right;
				image_speed = PLAYER_IMAGE_SPEED
				hsp = MOVESPEED;
				break;
		}
	}
}