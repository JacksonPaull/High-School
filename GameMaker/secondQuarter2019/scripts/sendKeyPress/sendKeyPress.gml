/// @param key
/// @param player
/// @param socket
var playerNum = argument1;
var key = argument0;
var socket = argument2

show_debug_message("Sending data...\nPlayerNum: "+string(playerNum)+"\nKey: "+string(key))

var buff = buffer_create(16,buffer_grow,1);
buffer_seek(buff,buffer_seek_start,0); //set buffer to original position
buffer_write(buff,buffer_u8,MOVEMENT) //identify movement key
buffer_write(buff,buffer_u8,playerNum) //playernum
buffer_write(buff,buffer_string,key) //movement key

network_send_packet(socket,buff,buffer_tell(buff))
buffer_delete(buff)