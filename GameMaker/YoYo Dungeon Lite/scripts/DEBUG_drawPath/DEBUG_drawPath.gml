path = argument0;
for(var i = 1; i<path_get_number(path);i++)
{
	draw_line(path_get_point_x(path,i-1),path_get_point_y(path,i-1),path_get_point_x(path,i),path_get_point_y(path,i));
}