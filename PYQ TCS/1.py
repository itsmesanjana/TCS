# Q1. Problem Statement –
# Given a string S (input consisting) of ‘*’ and ‘#’. The length of the string is variable. The task is
# to find the minimum number of ‘*’ or ‘#’ to make it a valid string. The string is considered
# valid if the number of ‘*’ and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
# Note: The output will be a positive or negative integer based on number of ‘*’ and ‘#’ in the
# input string.
# (*>#): positive integer
# (#>*): negative integer
# (#=*): 0
# Example 1:
# Input 1: ###*** -> Value of S
# Output : 0 → number of * and # are equal

def balance_symbols(S):
    stars=S.count('*')
    hashes=S.count('#')
    return stars-hashes

print(balance_symbols("###***"))  
print(balance_symbols("##***"))   
print(balance_symbols("####*"))  