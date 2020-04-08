
//Movement variables
inertia = 0.3 //Acts similar to mass
move_rate = 0 //Velocity
hovering = false


//slider variables
slidevar = -1
#macro slideWidth 100

var me = self
with(instance_create_layer(x+slideWidth+30,y,layer,obj_loopSlider))
{
	slider = me
}




