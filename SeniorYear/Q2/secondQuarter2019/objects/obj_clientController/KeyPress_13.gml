/// @description Send "Hello packet"
var t_buffer = buffer_create(256, buffer_grow, 1);
buffer_seek(t_buffer, buffer_seek_start, 0);
buffer_write(t_buffer , buffer_u16, MESSAGE);
buffer_write(t_buffer , buffer_string, "Hello");
network_send_packet(global.clientSocket, t_buffer, buffer_tell(t_buffer));
buffer_delete(t_buffer);