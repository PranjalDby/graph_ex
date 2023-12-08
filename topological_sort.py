def create_adj(edges,direction=0):
    adj = {}
    if direction == 0:
        for a,b in edges:
            if a not in adj:
                adj[a] = []

            if b not in adj:
                adj[b] = []

            adj[a].append(b)
            adj[b].append(a)

    else:
        for a,b in edges:
            if a not in adj:
                adj[a] = []
            
            if b not in adj:
                adj[b] = []

            adj[a].append(b)
    return adj

import queue

def topological_sort_kanhs(adj,src):

    visited = []
    in_degree = []
    for i in range(len(adj)+1):
        in_degree.append(0)
    
    q = queue.Queue(len(adj)+1)
    for i in adj:
        for j in adj[i]:
            in_degree[j] += 1

    
    # pushing the item into the queue with indegree 0
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            q.put(i)
    
    # doing BFS
    while not q.empty():
        node = q.get()
        visited.append(node)
        if node in adj:
            for v in adj[node]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.put(v)

    return visited[1:]

    
def topological_sort(adj,src,visited,ans=[]):
    if src not in visited:
        visited.append(src)

    for v in adj[src]:
        if v not in visited:
            topological_sort(adj,v,visited,ans)

    ans.append(src)
    return ans

edges = [[1,2],
         [1,3],
         [2,5],
         [3,5],
         [5,4]]
adj_list = create_adj(edges,1)

print(topological_sort_kanhs(adj_list,1))
