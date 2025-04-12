def sort_marbles(input_str):
    parts=list(map(int,input_str.strip().split()))
    n=parts[0]
    marbles=parts[1:]
    
    count0=marbles.count(0)
    count1=marbles.count(1)
    count2=marbles.count(2)

    sorted_marbles=[0]*count0+[1]*count1+[2]*count2

    return "".join(map(str,sorted_marbles))

print(sort_marbles("6 2 0 2 1 1 0"))  # Output: "0 0 1 1 2 2"
print(sort_marbles("5 1 2 0 1 0"))    # Output: "0 0 1 1 2"
 