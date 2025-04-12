def is_palindrome(s):
    return s==s[::-1]

def split_into_three_palindrome(word):
    n=len(word)
    
    for i in range(1,n-1):
        for j in range(i+1,n):
            s1=word[:i]
            s2=word[i:j]
            s3=word[j:]

            if is_palindrome(s1) and is_palindrome(s2) and is_palindrome(s3):
                print(s1)
                print(s2)
                print(s3)
    print("Impossible")
    
word=input().strip()
split_into_three_palindrome(word)