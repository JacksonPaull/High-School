hspeed = 0
vspeed = 0


if(keyboard_check(ord("W")))
{
	vspeed =-2
}
if(keyboard_check(ord("A")))
{
	hspeed = -2
}
if(keyboard_check(ord("S")))
{
	vspeed = 2
}
if(keyboard_check(ord("D")))
{
	hspeed = 2
}