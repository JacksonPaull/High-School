/*
	using the size of the place within the frame to draw
	take a sprite and determine a scale that maximizes its space in that frame without extending beyond it

*/

///@param canvasWidth
///@param canvasHeight
///@param spriteIndex

var canvasWidth = argument0
var canvasHeight = argument1
var sprite = argument2


var spriteHeight = sprite_get_height(sprite)
var spriteWidth = sprite_get_width(sprite)


return min(canvasWidth/spriteWidth,canvasHeight/spriteHeight)