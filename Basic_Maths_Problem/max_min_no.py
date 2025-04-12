def max_min_no(n):
    max_no=0
    min_no=9
    
    while(n):
        r=n%10
        
        max_no=max(r,max_no)
        
        min_no=min(r,min_no)
        
        n=n//10
    return max_no,min_no


n=2346
print(max_min_no(n))
# max_min_no(n)
