def second_largest(arr):
    first=-1
    second=-1
    
    for num in arr:
        if num>first:
            second=first
            first=num
        elif num<first and num>second:
            second=num
    return second