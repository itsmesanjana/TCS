def isPanagram(S):
    S=S.lower()
    seen=set()
    
    for ch in S:
        if 'a'<=ch<='z':
            seen.add(ch)
            
        return 1 if len(seen)==26 else 0
    
    
S=input()
print(isPanagram(S))