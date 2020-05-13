import heapq
import math

    
def distance(source,dest):
    return math.hypot(dest[0]-source[0],dest[1]-source[1])

def shortest_path(Map,source,dest):
    path_from={source:None}
    cost={source:0}
    frontier=[(0,source)]
    
    while len(frontier)>0 :
        current = heapq.heappop(frontier)[1]
        
        for adjacent in Map.roads[current]:
            
            new_cost = cost[current] + distance(Map.intersections[current],Map.intersections[adjacent])
            
            if adjacent not in path_from or new_cost < cost[adjacent]:
                
                cost[adjacent] = new_cost
                path_from[adjacent] = current
                heapq.heappush(frontier,(cost,adjacent))
                               
    return give_path(path_from, source, dest)               
                               
                               
def give_path(path_from,source,dest):
    
    path=[]
    current=dest
    while current!= source:
        path.append(current)
        current= path_from[current]
    path.append(source)
    
    return path[::-1]
