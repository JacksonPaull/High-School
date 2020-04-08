//Run through A* on current node

//add to closed list

//analyze adjacent nodes
//check whether we're at the end
//return next node


ds_list_add(closedList,getKey(nodeX,nodeY)); //adds nodes to closed list so it wont be processed again

var startToNode = ds_map_find_value(G,getKey(nodeX,nodeY));

pathMapWidth = array_length_1d(pathMap);
for(var r=max(nodeX-1,0);r<=min(nodeX+1,pathMapWidth-1);r++) //loop through all adjacent nodes within the field
{	
	pathMapHeight = array_length_2d(pathMap,r);
	for(var c=max(nodeY-1,0);c<=min(nodeY+1,pathMapHeight-1);c++)
	{
		if(r==nodeX && c == nodeY)
			continue;
		var closed = ds_list_find_index(closedList,getKey(r,c))!=-1;
		var diagonal = ((r+c)%2 ==(nodeX+nodeY)%2);
		var canWalk = false;
		if(diagonal){
			canWalk=pathMap[r,c]&&pathMap[nodeX,c]&&pathMap[r,nodeY];
		}
		else{
			canWalk=pathMap[r,c];	
		}
		if(!closed && canWalk)
		{
			//Create G
			var nodeToRC;
			if(diagonal)
				nodeToRC = 1.414;//sqrt 2, distance on diagonals with the length of 1 GRID_SIZE
			else
				nodeToRC=1;
			var nodeG = startToNode + nodeToRC;
			
			//create H
			var nodeH = abs(r-endX)+abs(c-endY);
			
			//create F
			var nodeF = nodeG+nodeH;
			
			//update if necessary
			var processed = ds_map_exists(G,getKey(r,c));
			
			if(processed){
				if(ds_map_find_value(G,getKey(r,c))>nodeG){//if the current G is better than the processed G
					ds_map_replace(G,getKey(r,c),nodeG);
					ds_map_replace(H,getKey(r,c),nodeH);
					ds_priority_change_priority(F,getKey(r,c),nodeF);
					ds_map_replace(parent,getKey(r,c),getKey(nodeX,nodeY));
				}
			}
			else{
				ds_map_add(G,getKey(r,c),nodeG);
				ds_map_add(H,getKey(r,c),nodeH);
				ds_priority_add(F,getKey(r,c),nodeF);
				ds_map_add(parent,getKey(r,c),getKey(nodeX,nodeY));
			}
		}
	}
}
var minF = -1;
var empty = ds_priority_empty(F);
if(!empty)
	minF = ds_priority_find_min(F);
	ds_priority_delete_min(F); // best node to move to

if(minF==-1){
	searching = false;
	found = false;
}
else{
	nodeX = getKeyX(minF);	
	nodeY = getKeyY(minF);	
}

if(nodeX == endX && nodeY == endY)
{
	searching = false;	
	found = true;
}
