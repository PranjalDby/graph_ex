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

def findParent(u,parent):
    if parent[u] == u:
        return u
    
    parent[u] = findParent(parent[u],parent)
    return parent[u]

def check_cyclic(adj):
    rank = []
    parent = []
    for i in range(len(adj) + 2):
        rank.append(0)
        parent.append(i)

    print(isCyclic(adj,parent,rank))
    print(parent)


def isCyclic(adj,parent,ranks) -> bool:
    for i in adj:
        for j in adj[i]:
                
                u = findParent(i,parent)
                v = findParent(j,parent)
                if u == v:
                    return True
                else:
                    Union(u,v,parent,ranks)

    return False



def Union(u,v,parent,ranks):
    u = findParent(u,parent)
    v = findParent(v,parent)

    if ranks[u] < ranks[v]:
        parent[u] = v

    elif ranks[v] < ranks[u]:
        parent[v] = u

    else:
        parent[v] = u
        ranks[u] += 1

edges = [
    [1,2],
    [2,4],
    [4,1],
    [2,5],
    [5,6],
    [5,7]
]
adj = addEdge(edges,0)


# Time complexity is 
"""

"""
# check_cyclic(adj)
