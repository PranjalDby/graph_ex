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


def largestComponent(adjL):
    visited  = set()
    count = 1
    maxi = 0
    for nodes in adjL:
        if nodes not in visited:
            count = dfs_count(nodes,adjL,visited)
            maxi = max(maxi,count)

    print(maxi)


def dfs_count(node,adjL,visited) -> int:
    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for neigh in adjL[node]:
        if neigh not in visited:
            size += dfs_count(neigh,adjL,visited)

    return size
edges = [
    [0,1],
    [0,8],
    [0,5],
    [5,8],

    [2,3],
    [2,4],
    [4,3],
]

adjL = addEdge(edges,0)
print(adjL)
largestComponent(adjL)