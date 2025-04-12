def get_min_max(arr):
    if len(arr)==0:
        return None
    
    min_val=arr[0]
    max_val=arr[0]
    
    for num in arr[1:]:
        if num<min_val:
            min_val=num
        if num>max_val:
            max_val=num
    return min_val,max_val

arr = [3, 2, 1, 56, 10000, 167]
min_val, max_val = get_min_max(arr)
print(min_val, max_val) 