# Insertion Sort is a type of sorting algorithm that places a unsorted element to its suitable position in an array in each iteration

def swap(a,b,items):
    t = items[b]
    items[b] = items[a]
    items[a] = t
    
def InsertionSort(arr,index,n):
    # Base case
    if index >= n:
        return
    
    # Processing
    firstelement = index-1
    key = index
    for i in range(index,n):
        if arr[key] < arr[firstelement]:
            swap(key,firstelement,arr)
        
        key += 1

    # RR
    InsertionSort(arr,index+1,n)


arr = [1,5,4,2,6,9,10,3]

InsertionSort(arr,1,len(arr))
print(arr)