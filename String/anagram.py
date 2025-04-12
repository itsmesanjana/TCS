def isanagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return "1"
    else:
        return "0"


s1=input()
s2=input()
print(isanagram(s1,s2))