def addEdge(edges,direction):
    adjList = dict()
    if direction == 0:
        # Undirected graph
        for u,v in edges:
            if u not in adjList:
                adjList[u] = []
            if v not in adjList:
                adjList[v] = []

            adjList[u].append(v)
            adjList[v].append(u)

    else:
        # Directed graph
        for u,v in edges:
            if u not in adjList:
                adjList[u] = []
            if v not in adjList:
                adjList[v] = []

            adjList[u].append(v)

    return adjList

# DFS
def detect_cycle(adj)->bool:
    visited = set()
    dfs_track = dict()
    for i in adj:
        if i not in visited:
            if dfs(adj,visited,i,dfs_track):
                return True

    return False

import queue
def detect_cycle_BFS(adj):
    visited = []
    for i in adj:
        if i not in visited:
            if topological_sort_kanhs(adj,i,visited):
                return True
            
    return False

def topological_sort_kanhs(adj,src,visited) -> bool:

    visited = []
    in_degree = []
    for i in range(len(adj)+1):
        in_degree.append(0)
    
    q = queue.Queue(len(adj)+1)
    # finding a node which is parent or src node
    for i in adj:
        for j in adj[i]:
            in_degree[j] += 1

    
    # pushing the item into the queue with indegree 0
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            q.put(i)
    
    # doing BFS
    while not q.empty():
        node = q.get()
        visited.append(node)
        if node in adj:
            for v in adj[node]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.put(v)

    if len(visited) == len(adj):
        return False
    
    return True

def dfs(adj,visited,node,dfs_track):
    visited.add(node)
    dfs_track[node] = True # keep track of the call of the node is gone or not
    for neigh in adj[node]:
        if neigh not in visited:
           cycle =  dfs(adj,visited,neigh,dfs_track)
           if cycle:
               return True
        elif neigh in visited and dfs_track[neigh]:
            return True
        
    dfs[node] = False
    return False
edges = [
    [1,2],
    [2,4],
    [2,3],
    [3,7],
    [3,8],
    [8,4],
    [4,5],
    [5,6],
    [6,4]
]

adj = addEdge(edges,1)
print(adj)

iscycle = detect_cycle_BFS(adj)
print(iscycle)

