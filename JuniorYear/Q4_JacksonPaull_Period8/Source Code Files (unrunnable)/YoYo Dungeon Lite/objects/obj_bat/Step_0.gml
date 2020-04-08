if(!init)
{
	generatePathMap();	
	startpath = path
	init = true;
	hp =5;
}

updateMobDirection();

if(hp<=0)
{
	instance_destroy();
}

//aggroInRange(aggroIn,aggroOut);