def is_prime( num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isSumofTwo(N):
    for i in range(2,N//2+1):
        if is_prime(i) and is_prime(N-i):
            return "Yes"
    return "No"


print(isSumofTwo(34))