def findParent(node,parent):
    if parent[node] == node:
        return node
    
    parent[node] = findParent(parent[node],parent) #path-compression
    return parent[node]

def unionSet(u,v,parent,rank):
    u = findParent(u,parent)
    v = findParent(v,parent)
    if rank[u] < rank[v]:
        parent[u] = v
    
    elif rank[v] < rank[u]:
        parent[v] = u
    
    else:
        parent[v] = u
        rank[u] += 1 

def makeSet(nodes):
    parent = [i for i in range(nodes + 1)]
    rank = [0] * (nodes + 1)
    edges = [
        [1,2,2],
        [1,4,1],
        [5,4,9],
        [1,5,4],
        [4,3,5],
        [2,3,3],
        [2,4,3],
        [2,6,7],
        [3,6,8],
    ]
    print(edges)
    # sort the above edgelist according to weights
    edges.sort(key=lambda x:x[-1])
    total_weight = 0
    for u,v,w in edges:
        u_parent = findParent(u,parent)
        v_parent = findParent(v,parent)
        if u_parent != v_parent:
            total_weight += w
            unionSet(u,v,parent,rank)

    return total_weight

if __name__ == "__main__":
    total = makeSet(7)
    print(total)