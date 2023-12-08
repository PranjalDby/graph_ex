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

from queue import Queue
def shortestPath(adjList,src,dest):
    visited = set()
    q = Queue()
    q.put((src,0))
    visited.add(src)
    prev_negh = 0
    while(not q.empty()):
        curr_pair = q.get()
        print("curr distance = {}".format(curr_pair))
        curr_node = curr_pair[0]
        curr_distance = curr_pair[1]
        if curr_node == dest:
            print(curr_pair,prev_negh)
            return curr_distance
        for nbr in adjList[curr_node]:
            if nbr not in visited:
                visited.add(nbr)
                prev_negh = curr_node
                q.put((nbr,curr_distance + 1))


    return -1
edges = [
    [1,2],
    [1,3],
    [3,2],
    [3,6],
    [2,6],
    [2,4],
    [6,4],
    [6,5],
    [5,4],
]
edges2 = [
    [1,2],
    [1,5],
    [2,3],
    [3,4],
    [5,6],
    [6,7],
    [7,4]
]
adjList = addEdge(edges,1)
print(adjList)
print(shortestPath(adjList,1,5))