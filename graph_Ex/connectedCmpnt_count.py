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

def count_connectedCmpnt(adj) -> int:
    count = 0
    for nodes in adj:
        if nodes not in visited:
            util_dfs(adj,nodes,visited)
            count += 1

    return count

def util_dfs(adj,src,visited):
    visited.add(src)
    for nbr in adj[src]:
        if nbr not in visited:
            visited.add(nbr)
            util_dfs(adj,nbr,visited)

edges = [
    [1,2],
    [4,6],
    [6,5],
    [6,7],
    [6,8],
    [3,-1],
]

adjL = addEdge(edges,0)
print(adjL)
print(count_connectedCmpnt(adjL))