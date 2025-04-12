# Min and Max in Array
# Difficulty: BasicAccuracy: 68.55%Submissions: 336K+Points: 1Average Time: 10m
# Given an array arr. Your task is to find the minimum and maximum elements in the array.

# Note: Return a Pair that contains two elements the first one will be a minimum element and the second will be a maximum.

# Examples:

# Input: arr[] = [3, 2, 1, 56, 10000, 167]
# Output: 1 10000
# Explanation: minimum and maximum elements of array are 1 and 10000.
# Input: arr[] = [1, 345, 234, 21, 56789]
# Output: 1 56789
# Explanation: minimum and maximum element of array are 1 and 56789.
# Input: arr[] = [56789]
# Output: 56789 56789
# Explanation: Since the array contains only one element so both min & max are same.
# Constraints:
# 1 <= arr.size() <= 105
# 1 <= arr[i] <=109

def min_max(arr):
    if len(arr)==0:
        return None
    min_val=arr[-1]
    max_val=arr[0]
    
    for num in arr[1:]:
        if num<min_val:
            min_val=num
        if num>max_val:
            max_val=num
    return (min_val,max_val)


arr=[1,4,5,2,7,9,100]
print(*min_max(arr))