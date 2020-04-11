draw_self();
draw_set_font(fnt);

for(var i =0;i<array_length_1d(buttonNames);i++)
{
	draw_text(room_width/2-50,300+(i*25),buttonNames[i]);
	if(buttonOn = i)
	{
		draw_text(room_width/2-75,300+(i*25),"->");	
	}
}