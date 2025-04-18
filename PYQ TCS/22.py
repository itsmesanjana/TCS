# Q22. An international round table conference will be held in india. Presidents from all over the
# world representing their respective countries will be attending the conference. The task is to find the
# possible number of ways(P) to make the N members sit around the circular table such that.
# The president and prime minister of India will always sit next to each other.
# Example 1:
# Input :
# 4 -> Value of N(No. of members)
# Output :
# 12 -> Possible ways of seating the members
# Explanation:
# 2 members should always be next to each other.
# So, 2 members can be in 2!ways
# Rest of the members can be arranged in (4-1)! ways.(1 is subtracted because the previously selected
# two members will be considered as single members now).
# So total possible ways 4 members can be seated around the circular table 2*6= 12.
# Hence, output is 12. Example 2:
# Input:
# 10 -> Value of N(No. of members)
# Output :
# 725760 -> Possible ways of seating the members
# Explanation:
# 2 members should always be next to each other.
# So, 2 members can be in 2! ways Rest of the members can be arranged in (10-1)! Ways. (1 is subtracted because the previously
# selected two members will be considered as a single member now).
# So, total possible ways 10 members can be seated around a round table is
# 2*362880 = 725760 ways.
# Hence, output is 725760. explain this question first and then give code


def factorial(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result

def count_seating_arr(N):
    if N<2:
        return "Invalid Input"
    return 2*factorial(N-1)
N=int(input().strip())
print(count_seating_arr(N))