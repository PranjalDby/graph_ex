def addEdge(edges,direction):
    adjList = dict()
    if direction == 0:
        for u,v in edges:
            if u not in adjList:
                adjList[u] = []

            if v!=-1 and v not in adjList:
                adjList[v] = []

            if v != -1:
                adjList[u].append(v)
                adjList[v].append(u)

    else:
        for u,v in edges:
            if u not in adjList:
                adjList[u] = []

            if v !=-1 and v not in adjList:
                adjList[v] = []
            
            adjList[u].append(v)

    return adjList

visited = set()
# DFS
def hasPath_un(adj,src,des):
    if src == des:
        return True
    # using dfs
    visited.add(src)
    for neigh in adj[src]:
        if neigh not in visited:
            if hasPath_un(adj,neigh,des):
                return True
            
    
    return False

# BFS - we assume that there should be cycle present in a graph
from queue import Queue
def has_pathBFS(adj,src,des):
    q = Queue(len(adj)+1)
    if src == des:
        return True
    
    if src not in visited:
        visited.add(src)
        
    q.put(src)
    
    while not q.empty():
        pop_curr = q.get()
        if pop_curr == des:
            return True
        for nbr in adj[pop_curr]:
            if nbr not in visited:
                visited.add(nbr)
                q.put(nbr)

    return False

# taking a undirected graph
ed_undire = [
    [1,2],
    [2,3],
    [3,1],
    [2,4],
    [4,5],
    [4,6],
    [7,-1]
]
ed_directed = [
    [1,2],
    [1,3],
    [2,6],
    [6,4],
    [3,5],
    [3,2],
    [4,3],
]
adj = addEdge(ed_directed,1)
print(adj)
print(has_pathBFS(adj,5,6))