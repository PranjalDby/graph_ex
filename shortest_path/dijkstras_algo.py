
def create_adj(edges,direction,nodes):
    adj = {c:[] for c in range(nodes+1)}
    if direction == 0:
        for a,b,w in edges:
            adj[a].append((b,w))
            adj[b].append((a,w))

    else:
            adj[a].append((b,w))

    return adj


import queue

def dijkstras(adj,src,nodes):
    q = queue.Queue(nodes + 1)
    distance = [float('inf')] * (nodes + 1)
    distance[src] = 0
    q.put((src,0))
    while(not q.empty()):
        curr,curr_w = q.get()                                                      
        for neigh in adj[curr]: # actual comparison to find the node with minimum weight on it
            des,w = neigh
            if distance[des] > curr_w + w:
                distance[des] = w + curr_w                    
                q.put((des,distance[des]))

    print(distance)


edges  = [
    [0,2,1],
    [0,1,7],
    [0,3,2],
    [1,2,3],
    [1,3,5],
    [1,4,1],
    [4,3,7]
]

adj_list = create_adj(edges,0,4)

dijkstras(adj_list,0,4)