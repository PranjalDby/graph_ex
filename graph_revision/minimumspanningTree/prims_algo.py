# works on undirected weighted graphs with no cycles present
def createAdj(edgeList,nodes):
    adjList = {c: [] for c in range(nodes + 1)}
    for u,v,w in edgeList:
        adjList[u].append((v,w))
        adjList[v].append((u,w))

    return adjList

import heapq
def MST(adjL,nodes,src):
    parent = [-1] * (nodes + 1) # parent gives our resultant MST
    visited = set() #track the node that are in mst or not
    rank:dict[int,list[int]] = {i:float('inf') for i in range(nodes + 1)} #priority-Queue implementation using dictionary
    print(rank)
    visited.add(src)
    rank[src] = 0
    while rank:
        node = min(rank,key=rank.get) #time complexity would be O(n) for n = nodes
        cost = rank[node]
        del rank[node]
        print(f'cost = {cost} for node = {node}')
        for nbr,w in adjL[node]:
            if nbr not in visited and rank[nbr] > w:
                rank[nbr] = w
                visited.add(nbr)
                parent[nbr] = node

    print(parent)

edgeList = [
    [0,1,2],
    [0,3,6],
    [1,3,8],
    [1,4,5],
    [1,2,3],
    [1,4,5],
    [4,2,7]
]
adjL = createAdj(edgeList,4)
print(adjL)
MST(adjL,4,0)