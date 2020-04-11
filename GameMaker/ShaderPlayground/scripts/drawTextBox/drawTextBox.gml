/*
Using spr_corner and spr_border, construct a border and text inside it

CURRENT NOTES:
Right now this draws outside of x2 and y2. Look at how rotation of sprites work and redefine the math to fix it.
*/

///@param x1 ..................Leftmost bound of the text box borders
///@param y1 ..................Uppermost bound of the text box borders
///@param x2 ..................Rightmost bound of the text box borders
///@param y2 ..................Bottommost bound of the text box borders
///@param scale ...............Scale of the borders of the text box (in multiples of 2 pixels)
///@param text ................Body text to be drawn
///@param font ................Font to be drawn in
///@param [*title*] ...........optional title argument
///@param [*titleFont*] .......optional titlefont
var title = -1
var titleFont = -1

//================================Parameters=============================================
#region

if(argument_count<7)
{
	show_debug_overlay(true)
	show_debug_message("NOT ENOUGH ARGUMENTS USED IN TEXT BOX DRAWING")
	show_debug_overlay(false)
	return "not enough variables"
}


var x1 = argument[0]
var y1 = argument[1]
var x2 = argument[2]
var y2 = argument[3]
var scale = argument[4]
var text = argument[5]
var font = argument[6]
if(argument_count >= 8)
{
	var title = argument[7]
	//Title argument passed
	if(argument_count >= 9)
	{
		//Title font passed
		var titleFont = argument[8]
	}
}
#macro FONT_FACTOR 3/5


#endregion



//===================================Draw Corners==============================================================================
#region

var cornerHeight = scale*sprite_get_height(spr_corner)
var cornerWidth = scale*sprite_get_width(spr_corner)

draw_sprite_ext(spr_corner,0,x1,y1,scale,scale,0,c_white,1)										//top left corner
draw_sprite_ext(spr_corner,0,x2,y1,-scale,scale,0,c_white,1)						//top right corner
draw_sprite_ext(spr_corner,0,x1,y2,scale,-scale,0,c_white,1)						//bottom left corner
draw_sprite_ext(spr_corner,0,x2,y2,-scale,-scale,0,c_white,1)			//top right corner

#endregion




//====================================Draw edges=================================================================================
#region

var borderScaleX = (x2-x1) - 2*cornerWidth
var borderScaleY = (y2-y1) - 2*cornerHeight

//CornerWidth and Height can be used to gather the edges of that stuff
draw_sprite_ext(spr_border,0,x1+cornerWidth,y1,borderScaleX,scale,0,c_white,1)					//Top border
draw_sprite_ext(spr_border,0,x1+cornerWidth,y2,-borderScaleX,scale,180,c_white,1)	//bottom border
draw_sprite_ext(spr_border,0,x1,y1+cornerHeight,-borderScaleY,scale,90,c_white,1)				//Left border
draw_sprite_ext(spr_border,0,x2,y1+cornerHeight,borderScaleY,scale,270,c_white,1)	//Right border

#endregion



//====================================Format text=================================================================================
#region

//The below defines the area which text is drawn within.
var textx1 = x1+cornerWidth
var textx2 = x2 - cornerWidth
var texty1 = y1+cornerHeight
var texty2 = y2 - cornerHeight


var words = [];
var currentWord = ""
var num = 0
for(var i = 1; i<=string_length(text);i++)
{
	//Loop through string and format it such that the words printed don't overflow outside of the defined area within to draw text
	var char = string_copy(text,i,1)
	if(char == " ")
	{
		words[num] = currentWord
		num++
		currentWord = ""
	}
	else
	{
		currentWord += char
	}
}
words[num] = currentWord


num = 0; //will hold current number of characters
currentWord = ""; //will hold the final string
for(i = 0; i<array_length_1d(words);i++)
{
	if(		(num+string_length(words[i]))*font_get_size(font)*FONT_FACTOR	> textx2-textx1	)
	{
		//Total number of characters is overflows the textbox
		currentWord+="#"
		num = 0
	}
	currentWord+=words[i]+" "
	num+=string_length(words[i])+1
}
//show_debug_message(currentWord)

currentWord = string_hash_to_newline(currentWord)

//show_debug_message(currentWord)

#endregion




//====================================Draw text=================================================================================
#region

draw_set_valign(fa_top)
draw_set_halign(fa_center)
draw_set_color(c_white)

if(title!=-1)
{
	//Title was passed
	if(titleFont!=-1)
	{
		//titleFont was passed
		draw_set_font(titleFont)
	}
	else
	{
		draw_set_font(font)
	}
	draw_text((textx1+textx2)/2,texty1,title)
}


//draw body text
draw_set_valign(fa_middle)
draw_set_font(font)
draw_text((textx1+textx2)/2,(texty1+texty2)/2,currentWord)

#endregion

