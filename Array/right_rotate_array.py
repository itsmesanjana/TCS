def right_rotate_array(arr, k):
    n = len(arr)
    k %= n

    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return arr

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(right_rotate_array(nums, k))
