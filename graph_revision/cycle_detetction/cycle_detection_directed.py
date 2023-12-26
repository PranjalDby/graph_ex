def add_egde(edges,nodes):
    adjL = {c:[] for c in range(nodes+1)}
    for u,v in edges:
        adjL[u].append(v)

    return adjL

def check_cycle(adjL,nodes) -> bool:
    visited = set()
    call_gone = []
    flag = False
    for i in adjL:
        if i not in visited:
            if dfs_isCycle(adjL,i,visited,call_gone):
                return True
            else:
                continue
    return False
    

def dfs_isCycle(al,node,visited,call_gone) -> bool:    
    visited.add(node)
    call_gone.append(node)
    for nbr in al[node]:
        if nbr not in visited:
            if dfs_isCycle(al,nbr,visited,call_gone):
                return True
        elif nbr in call_gone:
            return True
    
    call_gone.remove(node) # remove the node that call has already be gone
    return False

# Using kahn's algorithm
from queue import Queue
def topo_detectCycle(adjl,nodes) -> bool:
    visited = set()
    indegree = [0] * (nodes + 1)
    for i in adjl:
        for j in adjl[i]:
            indegree[j] += 1
    q = Queue()
    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.put(i)

    for n in range(nodes+1):
        if n in adjl and n not in visited:
            if bfs(adjl,n,visited,indegree,q):
                return True
            
    return False

def bfs(adjL,node,vis,indegree,q):
    vis.add(node)
    while not q.empty():
        currNode = q.get()
        vis.add(currNode)
        for nbr in adjL[currNode]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0:
                q.put(nbr) 
    
    # we traverse through all the vertices but no cycle is present
    if len(vis) == len(adjL):
        return False
    
    return True

edges = [
    [1,2],
    [1,3],
    [3,2],
    [2,4],
    [4,3]
]
# edges = [
#     [0,1],
#     [0,2],
#     [2,0],
#     [1,2],
#     [2,3]
# ]
adjl = add_egde(edges,4)
print(adjl)

# cycle -check
# print(check_cycle(adjl,4))
print(topo_detectCycle(adjl,4))