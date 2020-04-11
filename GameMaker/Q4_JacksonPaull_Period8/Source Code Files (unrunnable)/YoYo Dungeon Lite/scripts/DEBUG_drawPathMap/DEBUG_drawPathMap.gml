draw_set_alpha(0.3);
var previousColor = draw_get_color();
draw_set_color(c_green);


for(var r = 0; r<ceil(room_width/GRID_SIZE);r+=1)
{
	for(var c = 0; c<ceil(room_height/GRID_SIZE);c+=1)
	{
		var xPixel = r*GRID_SIZE;
		var yPixel = c*GRID_SIZE;
		
		draw_rectangle(xPixel,yPixel,xPixel+GRID_SIZE,yPixel+GRID_SIZE,!pathMap[r,c]);
		
	}
}

draw_set_color(previousColor);