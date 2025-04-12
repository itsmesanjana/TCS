def perfect_no(n):
    if n<2:
        return False
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    return total==n

print(perfect_no(6))