
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


import queue

def dijkstras(adj,src):
    q = queue.Queue(len(adj)+1)
    visited = []
    distance = []
    for i in range(len(adj)+1):
        distance.append(float('inf'))

    distance[src] = 0
    q.put((src,0))
    while(not q.empty()):
        curr,curr_w = q.get()
        if curr not in visited:
            visited.append(curr)                                                       
        for neigh in adj[curr]: # actual comparison to find the node with minimum weight on it
            des,w = neigh
            if distance[des] > curr_w + w:
                distance[des] = w + curr_w                    
                q.put((des,distance[des]))

    print(distance)
    print(visited)



edges = [
    [0,1,2],
    [0,2,6],
    [1,3,5],
    [2,3,8],
    [3,5,15],
    [3,4,10],
    [5,4,6],
    [4,6,2],
    [5,6,6]
]

adj_list = create_adj(edges,1)

dijkstras(adj_list,0)