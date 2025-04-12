def prime_no(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def AllPrimeFactors(N):
    result=[]
    for i in range(2,N+1):
        if prime_no(i) and N%i==0:
            result.append(i)
            while N%i==0:
                N//=i
        if N==1:
            break
        
    return result


print(AllPrimeFactors(100))  # Output: [2, 5]
print(AllPrimeFactors(35))   # Output: [5, 7]
print(AllPrimeFactors(84))   # Output: [2, 3, 7]
