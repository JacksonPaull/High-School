//@description- Ween

var aggroRange = argument0;
var deAggroRange = argument1;
var playerNode = getKey(obj_player.x,obj_player.y);

//determine if aggro'd
if(distance_to_object(obj_player)<aggroRange)
{
	aggroindex = true;
	restarted = false;
}
else if(distance_to_object(obj_player)>deAggroRange)
{
	aggroindex = false;
}


if(aggroindex == true)
{
	if(!((((x-obj_player.x) div GRID_SIZE)==0)&&(((y-obj_player.y) div GRID_SIZE)==0)))
	{
		if(pathMap[obj_player.x div GRID_SIZE, obj_player.y div GRID_SIZE])
		{
			pathToX = obj_player.x;
			pathToY = obj_player.y;
		}
	
		newPath = pathfindToObject(pathToX,pathToY);
	
		if(newPath!=path){
			path=newPath;
			if(path==-1)
				aggroindex=false;
			else
				path_start(path,movespeed*60,path_action_stop,false);
		}
	}
	
}

else if(aggroindex == false)
{
	
	if(restarted == false){
		if((((x-startX) div GRID_SIZE)==0)&&(((y-startY) div GRID_SIZE)==0))	
		{
			restarted = true;
			path=startpath;			
			path_start(path,movespeed,path_action_restart,false);
		}
		else
		{
			path= pathfindToObject(startX,startY);
			path_start(path,movespeed*30,path_action_stop,false);
		}
	}
	
}
