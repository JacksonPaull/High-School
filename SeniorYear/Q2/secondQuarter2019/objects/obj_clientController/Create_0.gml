global.clientSocket = network_create_socket(network_socket_tcp)
global.connectIP = "192.168.1.162"
var server = network_connect(global.clientSocket,global.connectIP,6510)
if server < 0
{
	show_debug_message("Connection Failed")	
}
