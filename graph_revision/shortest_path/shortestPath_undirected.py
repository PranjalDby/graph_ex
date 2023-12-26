def add_Edge(edges,nodes):
    adj = {c:[] for c in range(nodes + 1)}
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    return adj

# Using BFS
from queue import Queue
def shortest_path(adjL,nodes,src,dest) -> list[int]:
    q = Queue(nodes + 1)
    parent = [0] * (nodes + 1)
    visited = set()
    ans = []
    q.put(src)
    def shortedPathBFS(node):
        while not q.empty():
            front = q.get()
            for nbr in adjL[front]:
                if nbr not in visited:
                    visited.add(nbr)
                    q.put(nbr)
                    parent[nbr] = front

    parent[src] = -1
    visited.add(src)
    for i in adjL:
        if i not in visited:
            shortedPathBFS(i)

    currNode = dest
    ans.append(currNode)
    while currNode != src:
        currNode = parent[currNode]
        ans.append(currNode)
    return ans[::-1]

edges = [
    [1,2],
    [1,3],
    [3,8],
    [2,5],
    [5,8],
    [1,4],
    [4,6],
    [6,7],
    [7,8],
]
adjL = add_Edge(edges,8)
print(adjL)
print(shortest_path(adjL,nodes=8,src=1,dest=8))