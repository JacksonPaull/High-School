if(keyboard_check(upKey))
{
	playerMovement(playerNum,"up")
	sendKeyPress("up",playerNum,global.clientSocket)
}
else if(keyboard_check(leftKey))
{
	playerMovement(playerNum,"left")
	sendKeyPress("left",playerNum,global.clientSocket)
}
else if(keyboard_check(rightKey))
{
	playerMovement(playerNum,"right")
	sendKeyPress("right",playerNum,global.clientSocket)
}
else if(keyboard_check(downKey))
{
	playerMovement(playerNum,"down")
	sendKeyPress("down",playerNum,global.clientSocket)
}

