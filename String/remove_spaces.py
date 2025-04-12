def remove_spaces(s):
    return ''.join([ch for ch in s if ch!=" "])

s="geeks for  geeks"
print(remove_spaces(s))