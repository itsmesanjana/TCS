# Q19. Joseph is learning digital logic subject which will be for his next semester. He usually tries to
# solve unit assignment problems before the lecture. Today he got one tricky question. The problem
# statement is “A positive integer has been given as an input. Convert decimal value to binary
# representation. Toggle all bits of it after the most significant bit including the most significant bit.
# Print the positive integer value after toggling all bits”.
# Constrains1<=N<=100
# Example 1:
# Input :
# 10 -> Integer
# Output :
# 5 -> result- Integer
# Explanation:
# Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents
# “5”. Hence output will print “5”.

def toggle_bits(n):
    power=1<<(n.bit_length()) #Equivalent to 2^(bit_length)
    return (power-1)-n

n=int(input().strip())
if 1<=n<=100:
    print(toggle_bits(n))
else:
    print("Invalid Input")