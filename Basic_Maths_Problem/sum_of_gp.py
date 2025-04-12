def sum_of_gp(n,a,r):
    if r==1:
        return a*n
    return a*(r**n-1)//(r-1)

print(sum_of_gp(3,3,5))
