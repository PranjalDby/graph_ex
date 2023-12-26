def createAdj(edgeList,v):
    adj = {c:[] for c in range(v+1)}
    for u,v in edgeList:
        adj[u].append(v)
    
    return adj

def kosarajus(adjList,nodes,edgeList):
    visited = set()
    res = []
    linear_ordering = []
    def getTopological(adjList,node):
        visited.add(node)
        for nbr in adjList[node]:
            if nbr not in visited:
                visited.add(nbr)
                getTopological(adjList,nbr)
        
        linear_ordering.append(node)
    
    def dfs(adjList,node):
        visited.add(node)
        for nbr in adjList[node]:
            if nbr not in visited:
                visited.add(nbr)
                res.append(nbr)
                dfs(adjList,nbr)

    # done topological sort:- to get the linear ordering
    for i in range(nodes + 1):
        if i not in visited:
            getTopological(adjList,i)
    
    transposed_graph = {c:[] for c in range(len(adjList))}
    for u,v in edgeList:
        transposed_graph[v].append(u)

    count = 0
    visited.clear()
    while linear_ordering:
        top = linear_ordering.pop()
        print(top)
        if top not in visited:
            count+=1
            res.append(top)
            dfs(transposed_graph,top)

    print(res,count)


edgeList = [
    [0,1],
    [1,3],
    [1,2],
    [2,0],
    [3,4],
]

adjList = createAdj(edgeList,4)

kosarajus(adjList,4,edgeList)
