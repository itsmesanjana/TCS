# Q10. Airport security officials have confiscated several item of the passengers at the security check
# point. All the items
# have been dumped into a huge box (array). Each item possesses a certain amount of risk[0,1,2].
# Here, the risk severity of
# the items represent an array[] of N number of integer values. The task here is to sort the items based
# on their levels of
# risk in the array. The risk values range from 0 to 2.
# Example:
# Input:
# 7 -> Value of N
# [1,0,2,0,1,0,2]-> Element of arr[0] to arr[N-1], while input each element is separated by new line.
# Output :
# 0 0 0 1 1 2 2 -> Element after sorting based on risk severity

def sort_risk_levels(arr):
    count_0=arr.count(0)
    count_1=arr.count(1)
    count_2=arr.count(2)
    
    return [0]*count_0+[1]*count_1+[2]*count_2

n=int(input())
arr=[int(input()) for _ in range(n)]

print(*sort_risk_levels(arr))