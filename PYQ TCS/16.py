# Q16. A parking lot in a mall has RxC number of parking spaces. Each parking space will either
# be empty(0) or full(1). The status (0/1) of a parking space is represented as the element of the
# matrix. The task is to find index of the prpeinzta row(R) in the parking lot that has the most of the
# parking spaces full(1).
# Note :
# RxC- Size of the matrix
# Elements of the matrix M should be only 0 or 1.
# Example 1:
# Input :
# 3 -> Value of R(row)
# 3 -> value of C(column)
# [0 1 0 1 1 0 1 1 1] -> Elements of the array M[R][C] where each element is separated by new line.
# Output :
# 3 -> Row 3 has maximum number of 1’s

def max_ones(R,C):
    max_ones=-1
    max_row_index=-1
    
    for i in range(R):
        row=list(map(int,input().split()))
        count_ones=row.count(1)
        
        if count_ones>max_ones:
            max_ones=count_ones
            max_row_index=i+1 
            
    return max_row_index 
