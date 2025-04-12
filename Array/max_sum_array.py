def max_sum_arr(arr,k):#Sliding_windwo_tech

    n=len(arr)
    if n<k:
        return -1
    max_sum=curr_sum=sum(arr[:k])
    
    for i in range(k,n):
        curr_sum=curr_sum-arr[i-k]+arr[i]
        max_sum=max(max_sum,curr_sum)
    return max_sum

arr=[1,2,3,4,5,6,7]
k=4
print(max_sum_arr(arr,k))