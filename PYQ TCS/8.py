# Q8. Sort one array according to another array You are given two arrays a[] (integer) and b[] (char).
# The ith value of a[] corresponds to the ith value of b[].
# Sort the array b[] with respect to a[].
# Note: The output is whitespace and newline character sensitive. After every character print a
# whitespace character. Also do not print any newline character at any point.
# Example 1: Input: a[] = {3, 1, 2} b[] = {'G', 'E', 'K'}
# Output: E K G
# Explanation: Here 3 corresponds to G, 1 corresponds to 'E', 2 corresponds to 'K 

def sort_by_another_array(a,b):
    n=len(a)
    
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
                b[i],b[j]=b[j],b[i]
        
    for i in range(n):
        print(b[i],end=" ")

a = [3, 1, 2]
b = ['G', 'E', 'K']
sort_by_another_array(a, b)