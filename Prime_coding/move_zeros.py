def move_zeroes(arr):
    
    n=len(arr)
    j=0
    
    for i in range(n):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr

print(move_zeroes([1, 0, 2, 0, 3]))  # Output: [1, 2, 3, 0, 0]
