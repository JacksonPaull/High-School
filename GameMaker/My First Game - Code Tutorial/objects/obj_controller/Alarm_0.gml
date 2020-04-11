/// @description Insert description here
// You can write your code in this editor

//create enemy spawn and reset timer
instance_create_layer(random(room_width), random(room_height), "instances_enemies", obj_enemySpawn);
alarm[0] = spawnrate;