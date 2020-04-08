/// @param player
/// @param key
var key = argument1;
var player = argument0;
with(obj_player)
{
	if(playerNum==player)
	{
		//show_debug_message("Changing state for player "+string(player))
		switch key
		{
			case "up":
				image_index = 3;	
				break;
			case "down":
				image_index = 0;	
				break;
			case "left":
				image_index = 2;	
				break;
			case "right":
				image_index = 1;	
				break;	
		}
	}
}