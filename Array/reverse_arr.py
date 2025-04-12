def reverse_arr(arr):
    # n=len(arr)
    start=0
    end=len(arr)-1
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    
    return arr

arr=[1,2,3,4,5,6]
print(reverse_arr(arr))