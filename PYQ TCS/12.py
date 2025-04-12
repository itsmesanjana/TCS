# Q12. Jack is always excited about sunday. It is favourite day, when he gets to play all day. And goes to
# cycling with his friends.
# So every time when the months starts he counts the number of sundays he will get to enjoy.
# Considering
# the month can start with any day, be it Sunday, Monday…. Or so on.
# Count the number of Sunday jack will get within n number of days.
# Example 1:
# Input
# mon-> input String denoting the start of the month.
# 13 -> input integer denoting the number of days from the start of the month.
# Output :
# 2 -> number of days within 13 days.


def count_sundays(n,start_day):
    days=["sun","mon","tues","wed","thurs","fri","sat"]
    start_index=days.index(start_day)
    sunday_count=0
    for i in range(n):
        current_day=(start_index+i)%7
        if days[current_day]=="sun":
            sunday_count+=1
            
    return sunday_count

n = int(input("Enter number of days in month: "))
start_day = input("Enter starting day of month: ")

# Output
print("Number of Sundays:", count_sundays(n, start_day))
                