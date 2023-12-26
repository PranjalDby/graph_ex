# articulation point,vertex or cut vertex is node in unidirected graph which when removed form two or more componenets

def createAdjList(edges,nodes):
    adjL = {c:[] for c in range(nodes + 1)}
    for u,v in edges:
        adjL[u].append(v)
        adjL[v].append(u)
    
    return adjL

def findArticulation(adjL,nodes,src):
    visited = set()
    parent = -1
    low = [-1] * (nodes + 1)
    disc = [-1] * (nodes + 1)
    res = []
    timer = 0
    count_child = 0
    for i in range(nodes + 1):
        if i not in visited:
            doDFS(adjL,i,timer,visited,low,parent,disc,res,count_child)

    return res

def doDFS(adjL,node,timer,visited,low,parent,disc,res,count_child):
    visited.add(node)
    timer += 1
    disc[node] = low[node] = timer
    # get the adjacent nodes
    for nbr in adjL[node]:
        if nbr == parent:
            # if nbr is our parent then continue
            continue
        if nbr not in visited:
            count_child += 1
            doDFS(adjL,nbr,timer,visited,low,node,disc,res,count_child)
            # after recursion we have to update the low of the node
            low[node] = min(low[node],low[nbr])
            # Articulation point
            if low[nbr] >= disc[node] and parent != -1: #if node is not a src or root node
                res.append(node)
        else:
            # there is back-edge
            # update the low of node with minimum(low[node],dics[nbr]):
            low[node] = min(low[node],disc[nbr])

    # this is for root node or src node
    if parent == -1 and count_child > 1:
        res.append(node)

edges = [
    [0,3],
    [3,4],
    [4,0],
    [0,1],
    [1,2]
]
adjL = createAdjList(edges,4)
print(adjL)
res  = findArticulation(adjL,4,0)
print(res)

