def sum_of_cubes(N,M):
    total=sum(i**3 for i in range(N,M+1))
    return total
N=int(input("Enter the value of N:"))
M=int(input("Enter the value of M:"))

if N>M:
    print("Invalid input: N should be less than or equal to M.")
else:
    result=sum_of_cubes(N,M)
    print(f"Sum of cubes from {N} to {M} is:{result}")
