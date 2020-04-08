

//object calling begining position
beginX = x;
beginY = y;

//The object moving towards position
endX = argument0;
endY = argument1;

//Convert arguments to node values

beginX = beginX div GRID_SIZE;
beginY = beginY div GRID_SIZE;
endX = endX div GRID_SIZE;
endY = endY div GRID_SIZE;

//pre Algorithm

G = ds_map_create(); // Dist to begin
H = ds_map_create(); //Dist to finish
F = ds_priority_create(); //G+H
parent = ds_map_create(); //Node coming from
closedList = ds_list_create(); //Processed nodes

//init first G value
ds_map_add(G,getKey(beginX,beginY),0);


//algorithm
searching = true;
found = false;
nodeX = beginX;
nodeY = beginY;

while(searching){
	processCurrentNode();	
}


//endpoint is found or not
var path = -1;
if(found){
	path = path_add();
	var curNode=getKey(endX,endY);
	while(curNode!=getKey(beginX,beginY)){
			path_add_point(path,getKeyX(curNode)*GRID_SIZE+(GRID_SIZE/2),getKeyY(curNode)*GRID_SIZE+(GRID_SIZE/2),movespeed);
			curNode = ds_map_find_value(parent,curNode);
	}
	path_add_point(path,beginX*GRID_SIZE,beginY*GRID_SIZE,movespeed);
	path_reverse(path); //the path is built in reverse so the path is reversed
	path_set_closed(path,false); //make sure the path is open
}

//post alrgorithm
//destory datastructures
ds_map_destroy(G);
ds_map_destroy(H);
ds_priority_destroy(F);
ds_map_destroy(parent);
ds_list_destroy(closedList);

//return final path
return path;

beginX = beginX*GRID_SIZE;
beginY = beginY*GRID_SIZE;