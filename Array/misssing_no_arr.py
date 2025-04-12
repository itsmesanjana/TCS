def missing_no(arr):
    n=len(arr)+1
    total=n*(n+1)//2
    actual_sum=(sum(arr))
    return total-actual_sum

print(missing_no([1, 2, 3, 5]))          # Output: 4
print(missing_no([8, 2, 4, 5, 3, 7, 1])) # Output: 6
print(missing_no([1]))         