def addEdge(edges,nodes):
    adj = {c:[] for c in range(nodes + 1)}

    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    return adj

# Cycle Detection Using BFS
from queue import Queue
def BFS(adjL,nodes):
    parent = [-1] * (nodes + 1)
    visited = set()
    q = Queue()
    for i in adjL:
        if i not in visited:
           if  BFS_util(adjL,i,visited,parent,q):
               return True
           
    return False

def BFS_util(adjL,node,visited,parent,q:Queue):
    visited.add(node)
    q.put(node)
    while not q.empty():
        curr = q.get()

        for nbr in adjL[curr]:
            if parent[curr] == nbr and curr in visited:
                continue
            elif parent[nbr] == -1 and nbr not in visited:
                visited.add(curr)
                parent[nbr] = curr
                q.put(nbr)
            elif nbr != parent[curr] and curr in visited:
                return True
            
    return False
# Using DFS

def checkCycleDfs(adjL,node):
    parent = -1
    visited = set()
    for i in adjL:
        if i not in visited:
           if  dfs_util(adjL,i,visited,parent):
               return True
           
    return False

def dfs_util(adjL,node,visited,parent):
    visited.add(node)
    for nbr in adjL[node]:
        if nbr not in visited:
            if dfs_util(adjL,nbr,visited,node):
                return True
        
        else:
            if nbr != parent:
                return True
            
    return False

edges = [
    [0,1],
    [1,2],
    [0,2],
    [0,3],
    [3,4]
]

adjL = addEdge(edges,9)
print(adjL)

print(checkCycleDfs(adjL,9))
