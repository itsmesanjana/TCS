def right_rotate_array(nums,k):
    n=len(nums)
    k%=n
    return nums[-k:]+nums[:-k]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(right_rotate_array(nums, k))  # Output: [5, 6, 7, 1, 2, 3, 4]
