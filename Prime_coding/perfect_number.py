def is_perfect(num):
    sum_of_divisors=sum(i for i in range(1,num) if num%i==0)
    return sum_of_divisors==num

def perfect_numbers_in_range(N,M):
    return [i for i in range(N,M+1) if is_perfect(i)]

# Taking input from the user
N = int(input("Enter the value of N: "))
M = int(input("Enter the value of M: "))

# Ensuring N <= M
if N > M:
    print("Invalid input: N should be less than or equal to M.")
else:
    perfect_nums = perfect_numbers_in_range(N, M)
    if perfect_nums:
        print(f"Perfect numbers from {N} to {M} are: {perfect_nums}")
    else:
        print(f"No perfect numbers found in the range {N} to {M}.")


    