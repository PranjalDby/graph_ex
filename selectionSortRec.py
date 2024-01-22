# Selection Sort is type of sorting algorithm:
"""
it works by repeatidly selecting largest or smallest element from unsorted position of array or list or sequence and putting it into in
sorted portion.
it's time complexity is O(n**2)
"""

def swap(a,b,items):
    t = items[b]
    items[b] = items[a]
    items[a] = t

count = 0
def selectionSort(items,i,n):
    # Base Case
    global count;
    if i >= n:
        return
    
    for k in range(i+1,n):
        if items[k] < items[i]:
            swap(k,i,items)
    
    #RR
    
    selectionSort(items,i+1,n)


arr = [1,5,4,2,6,9,10,3]

selectionSort(arr,0,len(arr))

print(arr)