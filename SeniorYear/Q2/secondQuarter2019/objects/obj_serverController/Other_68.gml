var n_id = ds_map_find_value(async_load, "id") //ID of the connection
if n_id == serverSocket
{
	var type = ds_map_find_value(async_load, "type")
	switch(type)
        {
        case network_type_connect:
            var sock = ds_map_find_value(async_load, "socket");
            ds_list_add(socketlist, sock);
            break;
        case network_type_disconnect:
            var sock = ds_map_find_value(async_load, "socket");
            ds_map_delete(socketlist, sock);
            break;
		default:
			show_debug_message("ERROR IN CONNECTION")
			break;
        }
}
else if n_id = global.clientSocket
{
	show_debug_message("From local, do nothing")	
}
else if(ds_map_find_value(async_load,"type")==network_type_data)
	{
		var t_buffer = ds_map_find_value(async_load,"buffer")
		var cmd_type = buffer_read(t_buffer, buffer_u8);
		//show_debug_message(buffer_sizeof(t_buffer))
		switch (cmd_type)
		{
			case MESSAGE: 
				show_debug_message(buffer_read(t_buffer,buffer_string))
				buffer_delete(t_buffer)
				break;
			case MOVEMENT:
				var playerNum = buffer_read(t_buffer,buffer_u8)
				var key = buffer_read(t_buffer,buffer_string)
				show_debug_message("\nBuffer at server stage...\n PlayerNum: "+string(playerNum)+"\nKey: "+string(key)+"\n\n")
				bootlegSendToOthers(playerNum,key,n_id);
				//network_send_packet(20,t_buffer,buffer_tell(t_buffer))
				break;
			default:
				show_debug_message("ERROR IN DATA HANDLING")
				break;
		}
	}
