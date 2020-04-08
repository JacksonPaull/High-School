//Draw sidebar
draw_sprite_ext(spr_pixel,0,704,0,room_width-704,room_height,0,c_gray,0.6)

//Draw Info Room Info Text
//infoText = "This text is built to display informtion. Hopefully this is longer than needed to extend beyond the length of the box. Now I am writing a string that should extend beyond multiple lines and therefore contain multiple newlines at multiple different pixel coordinates to test the robustness of the algorithm thfsdfjdaskjfhasda fadsf sdaf"

drawTextBox(736,352,992,736,3,infoText,fnt_UI_rooms,title,fnt_UI_titles)
	
//Draw Room title
draw_set_font(fnt_roomTitle)
draw_set_color(c_white)
draw_set_alpha(1)
draw_set_halign(fa_center)
draw_set_valign(fa_middle)
var _roomName = room_get_name(room)
if(roomName != _roomName)
{
	roomName = _roomName
	title = "Room Info"
	global.activeShader = -1
	switch(_roomName)
	{
		case "rm_basicShaders":
			roomTitle = "Basic Shaders"
			infoText = "This room allows the testing of 6 small shaders. Click on a shader for more in depth comments on that shader."		
			break;
		case "rm_lighting":
			roomTitle = "Lighting"
			infoText = "This room showcases basic lighting. This is done by overlaying a slightly transparent black rectangle over the entire screen and punching holes in it over light sources."
			break;
	}
}
draw_text(863,63,roomTitle)
	