///@param layerNames (ds_list)

var layerNames = argument0

for(var i = 0; i<ds_list_size(layerNames);i++)
{
	layer_set_visible(layer_get_id(ds_list_find_value(layerNames,i)),false)
}
