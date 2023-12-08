def create_adj(edges,direction=0):
    adj = {}
    if direction == 0:
        for a,b,w in edges:
            if a not in adj:
                adj[a] = []

            if b not in adj:
                adj[b] = []

            adj[a].append((b,w))
            adj[b].append((a,w))

    else:
        for a,b,w in edges:
            if a not in adj:
                adj[a] = []
            
            if b not in adj:
                adj[b] = []

            adj[a].append((b,w))


    return adj

from collections import defaultdict
import heapq


def impL_prims(adj,src = 0):
    parent = [i for i in range(len(adj) + 1)]
    for i in range(len(parent)):
        parent[i] = -1
    
    parent[1] = -1
    mst = defaultdict(set)
    vsited =set([src])

    edge = [(src,node,weight) for node,weight in adj[src]]
    heapq.heapify(edge)

    vsited.add(src)
    while edge:
        u,v,weight = heapq.heappop(edge) #this give us the edge with min weight
        if v not in vsited:
            vsited.add(v)
            mst[u].add((v,weight))
            parent[v] = u
            # finding all the adjacent nodes for minimum node v
            for neigh,w in adj[v]:
                print(f'neigh in {v} = {neigh}')
                if neigh not in vsited:
                    heapq.heappush(edge,(v,neigh,w))
    
    print(parent)
    print(mst)

edges = [
    [0,1,2],
    [0,3,6],
    [3,1,8],
    [1,4,5],
    [1,2,3],
    [2,4,7],
  
]

adj = create_adj(edges,0)
impL_prims(adj)