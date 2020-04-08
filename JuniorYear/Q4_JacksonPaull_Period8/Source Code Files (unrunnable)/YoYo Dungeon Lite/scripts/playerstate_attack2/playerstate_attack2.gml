
if(firstTime)
{
	sprite_index = Baddie_Walk_Left;
	image_index = 0;
	image_speed = 0.5;
	firstTime = false;
	nextState = "idle";
	mask_index = Baddie_Walk_Left;
}


var hitByAttackNow = ds_list_create();
var hits = instance_place_list(x,y,obj_enemy,hitByAttackNow,false);
if hits>0
{
	for(var i = 0; i<hits;i++)
	{
		//if this instance has not been hit yet
		var hitID = hitByAttackNow[| i]; //shorthand for ds_list_find_value(hitByAttackNow,i)
		if(ds_list_find_index(hitByAttack,hitID) == -1)
		{
			ds_list_add(hitByAttack,hitID);
			with(hitID)
			{
				//whatever I want to do with the enemy
				//deal damage, make them flinch, change their sprite etc
				hp-=10;
			}
		}
	}
}

ds_list_destroy(hitByAttackNow);

if(animation_end())
{
	switchStates();
}
