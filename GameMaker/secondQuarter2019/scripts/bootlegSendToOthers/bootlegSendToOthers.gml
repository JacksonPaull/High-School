var playerNum = argument0
var key = argument1
var whoSent = argument2

var buff = buffer_create(16,buffer_grow,1)
buffer_seek(buff,buffer_seek_start,0)
buffer_write(buff,buffer_u8,MOVEMENT)
buffer_write(buff,buffer_u8,playerNum)
buffer_write(buff,buffer_string,key)

for(var i = 0; i<ds_list_size(socketlist); i++)
{
	if(ds_list_find_value(socketlist,i)!=serverSocket && ds_list_find_value(socketlist,i)!=whoSent)
	{
		show_debug_message("Sending data on socket "+string(ds_list_find_value(socketlist,i)))
		network_send_packet(ds_list_find_value(socketlist,i), buff, buffer_tell(buff))
	}
}
buffer_delete(buff)