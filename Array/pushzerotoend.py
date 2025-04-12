def pushzerotoend(arr):
    n=len(arr)
    j=0
    for i in range(n):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
arr=[0,0,0,1,2,3,4]
print(pushzerotoend(arr))