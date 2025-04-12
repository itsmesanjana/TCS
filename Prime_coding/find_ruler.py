# def find_ruler(n,families):
#     for fam in set(families):
#         if families.count(fam)>n//2:
#             return fam
#     return -1

# print(find_ruler(5, [2, 2, 1, 2, 2]))  # Output: 2
# print(find_ruler(4, [1, 2, 3, 4]))     # Output: -1

def find_ruler(n,families):
    for fam in set(families):
        if families.count(fam)>n//2:
            return fam
    return -1

print(find_ruler(5, [2, 2, 1, 2, 2]))  # Output: 2
print(find_ruler(4, [1, 2, 3, 4]))     # Output: -1
