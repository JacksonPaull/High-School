"""
    This file will contain the actual A* alg

    https://www.geeksforgeeks.org/a-search-algorithm/


Start at the source, generate all possible nodes to travel to, choose the one with the lowest f value
f = g + h
g = total distance from the start = parent.g + distance to parent
h = heuristic distance to goal. max(|goal.x - x|, |goal.y - y|)

1.  Initialize the open list
2.  Initialize the closed list
    put the starting node on the open 
    list (you can leave its f at zero)

3.  while the open list is not empty
    a) find the node with the least f on 
       the open list, call it "q"

    b) pop q off the open list
  
    c) generate q's 8 successors and set their 
       parents to q
   
    d) for each successor
        i) if successor is the goal, stop search
          successor.g = q.g + distance between 
                              successor and q
          successor.h = distance from goal to 
          successor (This can be done using many 
          ways, we will discuss three heuristics- 
          Manhattan, Diagonal and Euclidean 
          Heuristics)
          
          successor.f = successor.g + successor.h

        ii) if a node with the same position as 
            successor is in the OPEN list which has a 
           lower f than successor, skip this successor

        iii) if a node with the same position as 
            successor  is in the CLOSED list which has
            a lower f than successor, skip this successor
            otherwise, add  the node to the open list
     end (for loop)
  
    e) push q on the closed list
    end (while loop) 

"""
from math import *


class Node:
    def __init__(self, pos, end_pos, parent = None):
        self.pos = pos
        self.end_pos = end_pos
        self.parent = parent
        self.x = pos[0]
        self.y = pos[1]
        if parent is not None:
            #Not the origin
            self.g = parent.g + self.dist_to_node(parent)
            self.h = self.calculate_h(end_pos[0], end_pos[1])
            self.f = self.h + self.g
        else:
            self.f = self.g = self.h = 0
        
    def dist_to_node(self, node):
        #This function determines the euclidian distance between two nodes
        return sqrt(pow((node.x-self.x),2) + pow((node.y - self.y),2))

    def calculate_h(self, end_posx, end_posy):
        #best heuristic for determining which direction is good to check when we can move in 8 directions
        return max(abs(end_posx - self.x),abs(end_posy - self.y))

    def is_blocked(self, start_pos, end_pos, board, dx, dy):
        if end_pos in board.wall_list:
            return True
        
        if (end_pos[0], start_pos[1]) in board.wall_list and (start_pos[0], end_pos[1]) in board.wall_list:
            return True

        

    def generate_successors(self, board):
        #Generate a list of nodes around the current node that are not walls and are not on the closed list
        successor_list = []
        
        for i in range (-1,2):
            for j in range(-1,2):
                succx = self.x+i
                succy = self.y+j
                if succx >0 and succx < board.m and succy > 0 and succy< board.n:
                    successor_pos = (succx, succy)

                    if successor_pos == self.pos or self.is_blocked(self.pos, successor_pos, board, i, j):
                        pass #Don't create a successor as myself, or anything thats a wall
                    else:
                        #This position is not a wall and is in a different position
                        successor_list.append(Node(successor_pos, self.end_pos, self))
        return successor_list

    def trace_path(self):
        curr_path = [self.pos]
        
        if self.parent is not None:
            returned_list = self.parent.trace_path()
            if returned_list is not None:
                returned_list.append(self.pos)
                return returned_list
        return curr_path
        
        
        
def validate(node, _list):
    for list_node in _list:
        if list_node.pos == node.pos:
            if list_node.f > node.f:
                #This node is better than the other
                return _list.index(list_node)
            else:
                return -2
    return -1



def pathfind(board):
    """
        Arguments: board - 2D array representing the baord state, with integers representing the collision type
                    start_pos - tuple reperesenting the starting position
                    end_pos - tuple representing teh ending position
    """
    start_pos = board.start_pos
    end_pos = board.end_pos
    open_list = []
    closed_list = []

    q = Node(start_pos, end_pos)
    open_list.append(q)
    
    frame = 0

    

    while len(open_list) > 0:
        min_f = float("inf")
        for node in open_list:
            #Choose node with lowest f value to begin searching
            if node.f < min_f:
                q = node
                min_f = node.f

        open_list.remove(q)

        for node in q.generate_successors(board):
            if node.pos == end_pos:
                #Node is the goal
                return node.trace_path()#.append(node.pos)
            open_index = validate(node, open_list)
            closed_index = validate(node, closed_list)
            if open_index > -1:
                open_list.pop(open_index)
                open_list.insert(open_index, node)
            elif open_index == -1:
                open_list.append(node)
            
            if closed_index > -1:
                closed_list.pop(closed_index)
                closed_list.insert(closed_index, node)
            elif closed_index == -1:
                closed_list.append(node)
                
        closed_index = validate(q, closed_list)
        if closed_index > -1:
            closed_list.pop(closed_index)
            closed_list.insert(closed_index, q)
        elif closed_index == -1:
            closed_list.append(node)
    return []






