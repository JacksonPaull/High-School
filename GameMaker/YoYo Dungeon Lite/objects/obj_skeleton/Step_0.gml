if(!init){
	generatePathMap();
	if(path!=pointer_null)
	{
		startpath=path;	
		path_start(startpath,movespeed,path_action_restart,true);
	}
	
	init = true;
}

//Update the direction facing
updateMobDirection();

//Aggro onto the player within 70
aggroInRange(aggroIn,aggroOut);