var layerList = ds_list_create()
//Set all of the test layers to invisible
ds_list_add(layerList,"layer_textBoxTesting")
ds_list_add(layerList,"layer_uiTesting")
ds_list_add(layerList,"layer_bar")
ds_list_add(layerList, "layer_shaderLocations")
hideLayers(layerList)

ds_list_destroy(layerList)