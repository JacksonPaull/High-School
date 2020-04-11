/*
	This is intended to be given some parameters to determine where on the scale the slider is,
	and what min and max on a given scale that would be
*/

///@param sliderWidth
///@param min
///@param max

var sliderWidth = argument0
var _min = argument1
var _max = argument2


var percent = ((x-xstart)/sliderWidth+1)/2

return percent * (_max-_min) + _min