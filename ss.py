# Question  = Product of an array except self

arr = [2,3,4,5,6]

def product(arr):
    n = len(arr)
    ans = [1] * n
    for i in range(1,n):
       ans[i] = ans[i-1] * arr[i-1]

    right = arr[-1]
    for j in range(n-2,-1,-1):
        ans[j] = ans[j] * right
        right *= arr[j]
        
    return ans


print(product(arr))