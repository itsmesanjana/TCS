def is_sorted_arr(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
        
        
print(is_sorted_arr([10, 20, 30, 50,40]))    