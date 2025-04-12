def encrypt_string(s):
    compressed=""
    i=0
    while i<len(s):
        count=1
        while i+1<len(s) and s[i]==s[i+1]:
            count+=1
            i+=1
        compressed+=s[i]+str(count)
        i+=1
    return compressed[::-1]


s="broo"
print(encrypt_string(s))