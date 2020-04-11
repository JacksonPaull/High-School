/// @description Reconnect
var server = network_connect(global.clientSocket,global.connectIP,6510)
if server < 0
{
	show_debug_message("Connection Failed")	
}
