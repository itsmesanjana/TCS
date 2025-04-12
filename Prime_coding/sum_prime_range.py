def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def sum_of_primes(N,M):
    total=sum(i for i in range(N,M+1) if is_prime(i))
    return total

N=int(input("Enter the value of N:"))
M=int(input("Enter the value of M:"))

if N>M:
    print("Invalid input: N should be less than or equal to M.")
else:
    result=sum_of_primes(N,M)
    print(f"Sum of primes from {N} to {M} is:{result}")
# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2,int(num**0.5)+1 ):
#         if num%i==0:
#             return False
#     return True
# def sum_of_prime(N,M):
#     total=sum(i for i in range(N,M+1) if is_prime(i))
#     return total
# N=int(input("Enter the value of N:"))
# M=int(input("Enter the value of M:"))
# if N>M:
#     print("Invalid Input")
# else:
#     print(sum_of_prime(N,M))