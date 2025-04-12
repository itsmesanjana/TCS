def maxSubarraySum(arr):#using Kadane's algo
    
    max_sum=curr_sum=arr[0]
    for num in arr[1:]:
        curr_sum=max(num,curr_sum+num)
        max_sum=max(max_sum,curr_sum)
    return max_sum

arr=[1,2,3,4]
print(maxSubarraySum(arr))