def treasure_value(n,nums):
    max_val=max(nums)
    min_val=min(nums)
    return max_val-min_val


print(treasure_value(4, [10, 20, 30, 40]))  # Output: 30
print(treasure_value(5, [3, 8, 1, 9, 2]))   # Output: 8

