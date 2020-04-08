var xx = 32;
var yy = 32;
if gamepad_is_connected(controller)
    {
    draw_text(xx, yy, "Gamepad Slot - " + string(controller));
    draw_text(xx, yy + 20, "Gamepad Type - " + string(gamepad_get_description(controller)));
    draw_text(xx, yy + 40, "Left H Axis - " + string(gamepad_axis_value(controller, gp_axislh)));
    draw_text(xx, yy + 60, "Left V Axis - " + string(-gamepad_axis_value(controller, gp_axislv)));
    draw_text(xx, yy + 80, "Right H Axis - " + string(gamepad_axis_value(controller, gp_axisrh)));
    draw_text(xx, yy + 100, "Right V Axis - " + string(gamepad_axis_value(controller, gp_axisrv)));   
    draw_text(xx, yy + 120, "Fire Rate - " + string(gamepad_button_value(controller, gp_shoulderrb)));
    }
else
{
    draw_text(xx, yy, "Gamepad Slot - " + string(controller));
    draw_text(xx, yy + 20, "Gamepad not connected" + string(gamepad_get_description(controller)));
}

