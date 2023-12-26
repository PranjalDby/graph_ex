from collections import deque
class Node:
    def __init__(self,val = 0,neighbours = None):
        self.val = val
        self.neighbours = neighbours if neighbours is not None else []

    def __str__(self):
        return f"val = {self.val} nbr = {self.neighbours}"
    

from typing import Optional

class Solution:
    def clone(self,node:Optional['Node']) -> Optional['Node']:
        deepReff = Optional['Node'] # Node | None
        print(node.neighbours)



node:Optional['Node'] = Node(1,[Node(2),Node(4,[Node(1)])])

print(node.val)

print(node.neighbours[1].val)
q = deque([node])
q.append()
res = {node.val:Node(node.val,[])}
print(res[1].neighbours)

