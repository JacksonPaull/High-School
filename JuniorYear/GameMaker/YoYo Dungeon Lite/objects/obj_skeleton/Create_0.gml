//Animation and movement
path = pth_skeleton1;
movespeed = 1.5;
dir=DIR_LEFT;
xp = x;


//For restarting after de-aggro
startX = x;
startY = y;
restarted= true;

//Tiles the skeleton can't collide with
collisionTiles = [TILE_WATER,TILE_BRICK];

//aggro ranges
aggroIn = 70;
aggroOut = 120;
aggroindex = false;

//For initalizing all variables that need to be init after the object is drawn once
init = false;