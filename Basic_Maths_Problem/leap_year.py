def leap_year(n):
    return (n%4==0 and n%100!=0) or (n%400==0)

n=2004
print(leap_year(n))