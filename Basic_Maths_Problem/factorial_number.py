def factorial_no(n):
    # result=1
    # for i in range(1,n+1):
    #     result*=i
    # return result
    if n==0 or n==1:
        return 1
    return n*factorial_no(n-1)

n=4
print(factorial_no(n)) 