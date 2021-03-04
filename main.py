'''
Function tri_Traversal - performs DFS, UCS and A* traversals and returns the path for each of these traversals 

n - Number of nodes in the graph
m - Number of goals ( Can be more than 1)
1<=m<=n
Cost - Cost matrix for the graph of size (n+1)x(n+1)
IMP : The 0th row and 0th column is not considered as the starting index is from 1 and not 0. 
Refer the sample test case to understand this better

Heuristic - Heuristic list for the graph of size 'n+1' 
IMP : Ignore 0th index as nodes start from index value of 1
Refer the sample test case to understand this better

start_point - single start node
goals - list of size 'm' containing 'm' goals to reach from start_point

Return : A list containing a list of all traversals [[],[],[]]

NOTE : you MUST have three additional functions DFS_Traversal, UCS_Traversal and A_star_Traversal for each of the above mentioned traversals (DO NOT change the names of these individual functions).
'''
def Sort_Tuple(tup):  
  
    # reverse = None (Sorts in Ascending order)  
    # key is set to sort using second element of  
    # sublist lambda has been used  
    return sorted(tup, key = lambda x: x[1])
def check(f,x):
    flag=0
    for y in f:
        if(y[0]==x):
            flag=1
    return flag
def pop(frontier):
    # print(frontier)
    if(len(frontier)>1):
        
            for i in range(0,len(frontier)-1):
                if(frontier[i][1]<frontier[i+1][1]):
                    temp = frontier.pop(i)
                    return frontier,temp
            temp = frontier.pop(-1)
            return frontier,temp
        
    elif(len(frontier)==1):
        temp = frontier.pop(0)
        return frontier,temp


def calc_min(paths,cost):
    min_cost = 10000000
    temp = 0
    max1=0
    for i in paths:
        c=0
        g=len(i)
        for j in range(len(i)-1):
             c+=cost[i[j]][i[j+1]]
        # print(c)
        if(c<=min_cost and g>max1):
            min_cost=c
            max1=g
            # print(c)
            temp = i
            
    return temp
        

        



def a_star(cost,heuristic,start_point,goals):
    
    frontier = []
    frontier.append([start_point, heuristic[start_point]])
    came_from = {start_point: None}
    cost_so_far = {start_point: 0}
    has_been_next = []
    s=0
    vis = [0 for i in range(len(cost))]
    
    traverse = []

    while len(frontier)>0:
        frontier = Sort_Tuple(frontier)
        # print(frontier)
        frontier,curr = pop(frontier)
        vis[curr[0]]=1
      
        traverse.append(curr[0])
        if curr[0] in goals:
            s+=1
        if(s == 3):
            break
        neigh = []
        for x in range(len(cost)):
            if(vis[x]==0 and cost[curr[0]][x] not in [0,-1]):
                neigh.append(x)
        # print(curr[0],neigh)
        for next_tile in neigh:

            if next_tile not in has_been_next:
                has_been_next.append(next_tile)

            new_cost = cost_so_far[curr[0]] + cost[curr[0]][next_tile]
            if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                cost_so_far[next_tile] = new_cost
                priority = new_cost + heuristic[next_tile]
                if(check(frontier,next_tile)):
                    for y in frontier:
                        if(y[0]==next_tile):
                            y[1]=priority
                else:
                    frontier.append([next_tile, priority])
                came_from[next_tile] = curr[0]
    all_path = []
    # print(came_from)
    for k in goals:
        j1 = k
        path=[]
        while(j1!=None):
            
            path.append(j1)
            j1 = came_from[j1]
        all_path.append(path[::-1])
    # print(all_path)
    return calc_min(all_path,cost)

def dfs(cost,heuristic,start_point,goals):
    stack = []
    traverse = []
    came_from = {start_point:None}
    stack.append(start_point)
    s=0
    vis = [0 for i in range(len(cost))]
    while len(stack)>0:
        curr = stack.pop()
        vis[curr] = 1
        # print(curr)
        traverse.append(curr)
        if curr in goals:
            # s+=1
            break
            #return     
        if s==len(goals):
            break
        for j in range(len(cost)-1,0,-1):
            if(vis[j]==0 and cost[curr][j] not in [0,-1]):
                stack.append(j)
                came_from[j] = curr
                # vis[j]=1    
    return traverse 
    # all_path = []
    # # print(came_from)
    # for k in goals:
    #     j1 = k
    #     path=[]
    #     while(j1!=None):
            
    #         path.append(j1)
    #         j1 = came_from[j1]
    #     all_path.append(path[::-1])
    # # print(all_path)
    # return calc_min(all_path,cost)
def ucs(cost,heuristic,start_point,goals):
    frontier=[]
    frontier.append([start_point, 0])
    came_from = {start_point: None}
    cost_so_far = {start_point: 0}
    has_been_next = []
    s=0
    vis = [0 for i in range(len(cost))]
    
    traverse = []
    while len(frontier)>0:
        frontier=Sort_Tuple(frontier)
        frontier,curr = pop(frontier)
        vis[curr[0]]=1
        traverse.append(curr[0])
        if curr[0] in goals:
            s+=1
        if s==len(goals):
            break
        neigh = []
        for x in range(len(cost)):
            if(vis[x]==0 and cost[curr[0]][x] not in [0,-1]):
                neigh.append(x)
        # print(curr[0],neigh)
        for next_tile in neigh:

            if next_tile not in has_been_next:
                has_been_next.append(next_tile)

            new_cost = cost_so_far[curr[0]] + cost[curr[0]][next_tile]
            if next_tile not in cost_so_far or new_cost < cost_so_far[next_tile]:
                cost_so_far[next_tile] = new_cost
                priority = new_cost 
                if(check(frontier,next_tile)):
                    for y in frontier:
                        if(y[0]==next_tile):
                            y[1]=priority
                else:
                    frontier.append([next_tile, priority])
                came_from[next_tile] = curr[0]
    all_path = []
    # print(came_from)
    for k in goals:
        j1 = k
        path=[]
        while(j1!=None):
            
            path.append(j1)
            j1 = came_from[j1]
        all_path.append(path[::-1])
    # print(all_path)
    # print(traverse)
    return calc_min(all_path,cost)



# cost =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#             [0, 0, 5, 9, -1, 6, -1, -1, -1, -1, -1],
#             [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1], 
#             [0, -1, 2, 0, 1, -1, -1, -1, -1, -1, -1],
#             [0, 6, -1, -1, 0, -1, -1, 5, 7, -1, -1],
#             [0, -1, -1, -1, 2, 0, -1, -1, -1, 2, -1],
#             [0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
#             [0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1],
#             [0, -1, -1, -1, -1, 2, -1, -1, 0, -1, 8],
#             [0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 7],
#             [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]]
# heuristic = [0, 5, 7, 3, 4, 6, 0, 0, 6, 5, 0]
# dfs(cost,heuristic,1,[6,7,10])
def tri_Traversal(cost, heuristic, start_point, goals):
    l = []


    t1 = dfs(cost,heuristic,1,[6,7,10])
    t2 = ucs(cost,heuristic,1,[6,7,10])
    t3 = a_star(cost,heuristic,1,[6,7,10])

    l.append(t1)
    l.append(t2)
    l.append(t3)
    return l
# print(tri_Traversal(cost,heuristic,1,[6,7,10]))
