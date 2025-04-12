def armstrong_no(n):
    return n==sum(int(d)**3 for d in str(n))

print(armstrong_no(153))
