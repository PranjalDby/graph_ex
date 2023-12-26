def bellmanFord(edgeList,n,m ,src,dest):
    dist = [float('inf')] * (n + 1)
    dist[src] = 0
    for i in range(n+1):
        #travers on edge list
        for j in range(m):
            u,v,wt= edgeList[j]
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                dist[v] = dist[u] + wt

    # for one more time
    flag = 0
    for j in range(m):
        u,v,wt= edgeList[j]
        if dist[u] != float('inf') and dist[u] + wt < dist[v]:
            dist[v] = dist[u] + wt
            flag = 1

    if flag == 0:
        return dist[dest]
    
    return -1


# edges = [
#     [0,1,5],
#     [0,2,3],
#     [1,2,2],
#     [1,3,6],
#     [2,3,7],
#     [2,4,4],
#     [3,4,-1],
#     [2,5,2],
#     [4,5,-2],
# ]
edges = [
    [0,1,5],
    [0,2,-1],
    [2,1,-4],
    [1,4,2],
    [4,2,-3],
    [1,3,6]
]
# print(edges)
src = 2
des = 4
res = bellmanFord(edges,4,6,src,des)
if res != -1:
    print(f'distance from {src} -> {des} = {res}')

else:
    print(f'there is a negative cycle present b/w {src} -> {des}')