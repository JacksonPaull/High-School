   ///@param font <fnt_>
///@param options <Array>

var fnt = argument0
var menuOptions = argument1
var fntSize = font_get_size(fnt);
var portHeight = surface_get_height(application_surface)
var portWidth = surface_get_width(application_surface)


//Set prerequisites
draw_set_color(c_white)
draw_set_halign(fa_center)
draw_set_font(fnt)
draw_set_alpha(1)

//draw options
for (var i = 0; i < array_length_1d(menuOptions); ++i) 
{
    draw_text(portWidth/2,(portHeight/2-fntSize*array_length_1d(menuOptions)/2)+fntSize*2*i,menuOptions[i]);
}


//draw indicator
var triX = portWidth/2-string_length(menuOptions[menuIndex])/2*fntSize-40;
var triY = portHeight/2-fntSize*array_length_1d(menuOptions)/2+fntSize*2*menuIndex+fntSize/2;
draw_triangle(triX,triY+20,
			  triX,triY-20,
			  triX+40,triY,
			  false);