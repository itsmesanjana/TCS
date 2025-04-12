def binary_to_decimal(b):
    decimal=0
    for digit in b:
        decimal=decimal*2+int(digit)
    return decimal 

print(binary_to_decimal("111"))  