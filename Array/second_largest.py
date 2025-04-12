 # Second Largest
# Difficulty: EasyAccuracy: 26.72%Submissions: 1.1MPoints: 2Average Time: 15m
# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.
# Constraints:
# 2 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 105

# Expected C

def second_largest_ele(arr):
    first=-1
    second=-1
    
    for num in arr:
        if num>first:
            second=first
            first=num
        elif num<first and num>second:
            second=num
    return second

arr=[1,2,3,45,6,7,89,450]
print(second_largest_ele(arr))
            