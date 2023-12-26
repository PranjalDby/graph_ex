def createAdjList(edgelist,n):
    adjList = {c:[] for c in range(n+1)}
    for u,v in edgelist:
        adjList[u].append(v)
        adjList[v].append(u)

    return adjList

def findBridge(adjList,n,src):
    visited = set()
    parent = -1
    disc = [-1] * (n+1)
    low = [-1] * (n+1)
    ans = []
    t = 0
    for i in range(n+1):
        if i not in visited:
            doDfs(adjList,i,visited,parent,low,disc,ans,t)

    return ans

def doDfs(adjL,node,visited,parent,low,disc,ans,timer):
    visited.add(node)
    timer += 1
    disc[node] = low[node] = timer
    for nbr in adjL[node]:
        if nbr == parent:
            continue
        if nbr not in visited:
            doDfs(adjL,nbr,visited,node,low,disc,ans,timer)
            #after return from call we update the low of parent of child node
            low[node] = min(low[node],low[nbr])
            # check edge is bridge
            if low[nbr] > disc[node]:
                print('Find bridge')
                ans.append((node,nbr))
        else:
            # if there is back edge
            low[node] = min(low[node],disc[nbr])

edgelist = [
    [0,1],
    [1,2],
    [0,2],
    [0,3],
    [3,4]
]
adjList = createAdjList(edgelist,4)
print(adjList)
# bridge

print(findBridge(adjList,4,0))