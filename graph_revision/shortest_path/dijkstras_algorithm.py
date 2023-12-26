def createEdge(edges,nodes):
    adjL = {c:[] for c in range(nodes + 1)}
    for u,v,w in edges:
        adjL[u].append((v,w))
        adjL[v].append((u,w))

    return adjL

def dijkstras_algo(adjL,nodes,src):
    pair = set()
    visited = set()
    distance = [float('inf')] * (nodes + 1)
    distance[src] = 0
    pair.add((src,0))
    for i in range(nodes+1):
        if i not in visited:
            dijkstras_algoHelper(adjL,i,visited,pair,distance)

    print(distance)

from queue import Queue
def dijkstras_algoHelper(adjL,n,visited,pair:set,distance):
    visited.add(n)
    while len(pair) != 0:
        fetc_top = pair.pop()
        top_node,wt = fetc_top
        # traverse on nbrs
        for nbr, nbr_wt in adjL[top_node]:
            if (wt + nbr_wt) < distance[nbr]:
                if (nbr,nbr_wt) in pair:
                    pair.remove((nbr,nbr_wt))
                distance[nbr] = (wt + nbr_wt)
                pair.add((nbr,distance[nbr]))



edges  = [
    [0,2,1],
    [0,1,7],
    [0,3,2],
    [1,2,3],
    [1,3,5],
    [1,4,1],
    [4,3,7]
]

aList = createEdge(edges,4)
print(aList)
# dijkstras_algo(aList,4,0)
stes = {(1,2),(0,0),(2,8),(4,3)}
el = stes.pop()
print(el)