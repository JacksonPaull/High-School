if(keyboard_check_pressed(ord("W")) || (gamepad_axis_value(global.controller,gp_axislv)<0) || gamepad_button_check_pressed(global.controller,gp_padu))
	return "up"
	
if(keyboard_check_pressed(ord("S")) || (gamepad_axis_value(global.controller,gp_axislv)>0)|| gamepad_button_check_pressed(global.controller,gp_padd))
	return "down"
	
if(keyboard_check_pressed(ord("A")) || (gamepad_axis_value(global.controller,gp_axislh)<0)|| gamepad_button_check_pressed(global.controller,gp_padl))
	return "left"
	
if(keyboard_check_pressed(ord("D")) || (gamepad_axis_value(global.controller,gp_axislh)>0)|| gamepad_button_check_pressed(global.controller,gp_padr))
	return "right"
	
if(keyboard_check_pressed(vk_enter) || (gamepad_button_check_pressed(global.controller,gp_face1)))
	return "enter"
	
if(keyboard_check_pressed(vk_escape) || (gamepad_button_check_pressed(global.controller,gp_select)))
	return "escape"