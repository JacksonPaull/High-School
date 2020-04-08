/// @description Insert description here
// You can write your code in this editor

//moves the enemy towards the player, but first checks it exists to prevent errors
if (instance_exists(obj_player))
{
    move_towards_point(obj_player.x, obj_player.y, spd);
}

//direction=point_direction(x,y,obj_player.x,obj_player.y);
image_angle=direction;

if(hp<=0){
	with(obj_score){
		theScore+=5;	
	}
	//THIS SOUND CAN BE ADDED IN BUT IS REALLY ANNOYING
	//audio_sound_pitch(snd_death, random_range(0.8, 1.2));
	//audio_play_sound(snd_death,1,false);
	instance_destroy();
}