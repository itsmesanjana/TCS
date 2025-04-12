def findSubstring(txt,prt):
    n=len(txt)
    m=len(prt)
    
    for i in range(n-m+1):
        if txt[i:i+m]==prt:
            return i 
    return -1


txt = "geeksforgeeks"  # length = 13 → n = 13
prt = "eks"            # length = 3 → m = 3
print(findSubstring(txt,prt))