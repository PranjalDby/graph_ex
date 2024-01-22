# It is a type of Sorting algorithm which sorts elements of an array by repeaditly swaping the element with its adjacent ones,if they are in wrong order.
# Main motive is to push the larger to element to the right hand side

# time complexity = theta(n**2)

def swap(a,b,items):
    t = items[b]
    items[b] = items[a]
    items[a] = t  

def bubbleSort(items,n):
    # Base Case
    if n == 1 or n ==0:
        return
    
    # Processing 
    # Largest Element ko end par pahuchana hai
    for i in range(n-1):
        if items[i] > items[i+1]:
            swap(i,i+1,items)
    
    # RR
    # to yha par hame pata hai ki largest element vo apne sahi position par pahuch gya hai to ham phir recursive call kare items size - 1 par
            
    bubbleSort(items,n-1)



arr = [1,5,4,2,6,9,10,3]

n = len(arr)

bubbleSort(arr,n)
print(arr)

