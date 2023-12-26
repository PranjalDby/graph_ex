
def findParent(parent:list[int],u:int):
    if parent[u] == u:
        return u

    parent[u] = findParent(parent,parent[u])

    return parent[u]

def Union(u:int,v:int,ranks:list[int],parent:list[int]):
    u = findParent(parent,u)
    v = findParent(parent,v)
    if ranks[u] < ranks[v]:
        parent[u] = v

    elif ranks[v] < ranks[u]:
        parent[v] = u

    else:
        parent[v] = u
        ranks[u] += 1


def kruskals(edges,n):
    sorted_weight = [] # a linear data structure which holds the edges with minimum weight on it which comes first
    parent = []
    rank = []
    for i in range(n+1):
        parent.append(i)
        rank.append(0)


    for ed in edges:
        sorted_weight.append(ed)

    sorted_weight.sort(key=lambda x : x[-1])
    minW = 0
    for k in sorted_weight:
        u = findParent(parent,k[0])
        v = findParent(parent,k[1])
        if u != v:
            minW += k[2]
            Union(u,v,rank,parent)

    print(f"MST {parent} with total_weight = {minW}")


#edge list in form of [u,v,w]
edges = [
    [4,5,9],
    [1,5,4],
    [1,4,1],
    [4,2,3],
    [1,2,2],
    [4,3,5],
    [3,2,3],
    [3,6,8],
    [2,6,7]
    ]

no_nodes = 6
# print(edges)
kruskals(edges,no_nodes)