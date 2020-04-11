shader = shdr_dayAndNight
application_surface_draw_enable(false)
u_col = shader_get_uniform(shader,"col")
u_con_sat_brt = shader_get_uniform(shader, "con_sat_brt")

color_mix = -1;
color[0,0] = undefined;

con_sat_brt_mix = -1

key_previous = -1
key_next = -1;



//Add key times
scr_addKeyTime(010,070,200,0.7,0.6,0.00,5.00,0.67) //midnight
scr_addKeyTime(010,080,220,0.8,0.9,0.00,2.0,0.75) //late night
scr_addKeyTime(250,235,200,1.1,1.3,0.05,0.8,0.8) //dawn
scr_addKeyTime(245,235,190,1.1,1.1,0.10,0.0,1.0) //morning
scr_addKeyTime(255,250,230,1.3,0.9,0.15,0.0,1.0) //noon
scr_addKeyTime(250,240,200,1.4,1.1,0.15,0.0,1.0) //late afternoon
scr_addKeyTime(215,150,220,1.4,1.3,0.20,0.8,0.8) //dusk
scr_addKeyTime(010,080,220,0.9,0.9,0.00,2.0,0.75) //early night


keyTimeNum = array_height_2d(color)

//water reflcetion
var lyr_reflection = layer_get_id("tile_reflection")
layer_script_begin(lyr_reflection, scr_set_alpha)
layer_script_end(lyr_reflection, scr_reset_alpha)

u_alpha = shader_get_uniform(shdr_alpha, "alpha")
alpha = 0