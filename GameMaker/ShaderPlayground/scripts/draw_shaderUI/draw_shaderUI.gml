///@param info
///@param title5
var info = argument0
var title = argument1
var _y = y+sprite_get_height(spr_frame)/2

draw_sprite(spr_frame,0,x,y)
draw_set_halign(fa_center)
draw_set_valign(fa_middle)
draw_set_font(fnt_UI_rooms)
draw_text(x,y-sprite_get_height(spr_frame)/3,title)
drawTextBox(x-sprite_get_width(spr_frame)/2+10,_y-drawSpaceHeight+10,x+sprite_get_width(spr_frame)/2-10,_y+drawSpaceWidth/2,2,info,fnt_arial8)