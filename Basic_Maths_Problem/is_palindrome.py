# Palindrome
# Difficulty: EasyAccuracy: 56.28%Submissions: 100K+Points: 2
# You are given an integer n. Your task is to determine whether it is a palindrome.

# A number is considered a palindrome if it reads the same backward as forward, like the string examples "MADAM" or "MOM".

# Examples:

# Input: n = 555
# Output: true
# Explanation: The number 555 reads the same backward as forward, so it is a palindrome.
# Input: n = 123
# Output: false
# Explanation: The number 123 reads differently backward (321), so it is not a palindrome.
# Input: n = 1221
# Output: true
# Constraints:
# 1 <= n <= 109


def is_palindrome(n):
    return str(n)==str(n)[::-1]

n=121
print(is_palindrome(n))