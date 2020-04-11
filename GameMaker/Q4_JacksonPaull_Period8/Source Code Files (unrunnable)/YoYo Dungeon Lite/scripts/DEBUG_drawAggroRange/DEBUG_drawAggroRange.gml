var aggroIn = argument0;
var aggroOut = argument1;


//draw Aggro Range
draw_set_alpha(0.7);
for(var i=aggroIn; i>aggroIn-2; i-=0.5)
{
	draw_circle_color(x,y,i,c_red,c_red,true);
}

//Draw De-aggro Range
for(var i=aggroOut; i>aggroOut-2; i-=0.5)
{
	draw_circle_color(x,y,i,c_green,c_green,true);
}