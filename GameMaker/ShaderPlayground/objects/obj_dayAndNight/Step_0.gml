//mix colors

//Get key times:
var time = global.slider1
key_previous = min(floor(time*keyTimeNum), keyTimeNum - 1)
key_next = (key_previous+1) mod keyTimeNum

//get lerp amounts
var lerp_amt = (time - key_previous/keyTimeNum) * keyTimeNum

//mix colors
color_mix = [lerp(color[key_previous,0],color[key_next,0],lerp_amt),
				lerp(color[key_previous,1],color[key_next,1],lerp_amt),
				lerp(color[key_previous,2],color[key_next,2],lerp_amt)];
				
con_sat_brt_mix = [lerp(con_sat_brt[key_previous,0],con_sat_brt[key_next,0],lerp_amt),
				lerp(con_sat_brt[key_previous,1],con_sat_brt[key_next,1],lerp_amt),
				lerp(con_sat_brt[key_previous,2],con_sat_brt[key_next,2],lerp_amt),
				lerp(con_sat_brt[key_previous,3],con_sat_brt[key_next,3],lerp_amt),
				lerp(con_sat_brt[key_previous,4],con_sat_brt[key_next,4],lerp_amt)];




//reflection alpha
alpha = clamp(sin((2*global.slider1+0.5)*pi)*1.6-0.1,0,1)

