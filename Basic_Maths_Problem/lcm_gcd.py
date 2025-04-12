def lcm_gcd(a,b):
    def gcd(x,y):
        while y:
            x,y=y,x%y
        return x
    
    g=gcd(a,b)
    l=(a*b)//g
    return [l,g]

print(lcm_gcd(5, 10))