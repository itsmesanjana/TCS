def rotate_array(nums, k):
    n = len(nums)
    k %= n  # Handle k > n

    # Reverse helper
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Make a copy to avoid modifying original
    nums_copy = nums[:]
    
    reverse(nums_copy, 0, n - 1)
    reverse(nums_copy, 0, k - 1)
    reverse(nums_copy, k, n - 1)
    
    return nums_copy

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array(nums, k))  # Output: [5, 6, 7, 1, 2, 3, 4]
