/// @description Data from server
var n_id = ds_map_find_value(async_load, "id");
if n_id == global.clientSocket
{
	if ds_map_find_value(async_load,"type")==network_type_data
	{
		show_debug_message("Client recieved data")
		var buff = ds_map_find_value(async_load,"buffer")
		buffer_seek(buff,buffer_seek_start,0)
		var type = buffer_read(buff,buffer_u8)
		if(type==MOVEMENT)
		{
			var playerNum = buffer_read(buff,buffer_u8)
			var key = buffer_read(buff, buffer_string)
			show_debug_message("PlayerNum: "+string(playerNum)+"\nKey: "+string(key))
			playerMovement(playerNum, key)
		}
		buffer_delete(buff)
	}
} 