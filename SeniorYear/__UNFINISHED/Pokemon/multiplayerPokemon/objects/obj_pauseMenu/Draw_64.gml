if(global.pause)
{
	var width = surface_get_width(application_surface)
	var height = surface_get_height(application_surface)
	
	//Draw screen
	draw_set_alpha(1)
	draw_set_color(c_black)
	draw_rectangle(0,0,width,height,false)
	
	//Draw title
	draw_set_color(c_gray)
	draw_set_halign(fa_center)
	draw_set_font(fnt_pokemon_large)
<<<<<<< HEAD:Pokemon/multiplayerPokemon/objects/obj_pauseMenu/Draw_64.gml
	draw_text(width/2, height/4 + font_get_size(fnt_pokemon_large), "Game Paused")
=======
	draw_text(room_width/2, room_height/8+font_get_size(fnt_pokemon_large)*2, "Game Paused")
>>>>>>> 6847f693b08b055d3eaef613b22300478a0b99ad:Pokemon/multiplayerPokemon/objects/obj_pauseMenu/Draw_0.gml
	
	//Draw Menu
	drawBasicMenu(fnt_pause,menuOptions)	
}