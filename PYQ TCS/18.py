# Q18.
# Problem Statement
# A doctor has a clinic where he serves his patients. The doctor’s consultation fees are different for
# different groups of patients depending on their age. If the patient’s age is below 17, fees is 200 INR. If
# the patient’s age is between 17 and 40, fees is 400 INR. If patient’s age is above 40, fees is 300 INR.
# Write a code to calculate earnings in a day for which one array/List of values representing age of
# patients visited on that day is passed as input.
# Note:
#  Age should not be zero or less than zero or above 120
#  Doctor consults a maximum of 20 patients a day
#  Enter age value (press Enter without a value to stop):
# Example 1:
# Input
# 20
# 30
# 40
# 50
# 2
# 3
# 14
# Output
# Total Income 2000 INR
# Note: Input and Output Format should be same as given in the above example.
# For any wrong input display INVALID INPUT
# Output Format
# Total Income 2100 INR
def calculate_total_income():
    total_income=0
    patient_count=0
    
    while patient_count<20:
        age_input=input().strip()
        if age_input=="":
            break
        if not age_input.isdigit():
            print("Invalid Iinput")
            return 
        age=int(age_input)
        
        if age<1 and age>120:
             print("Invalid Input")
             return 
         
        if age<17:
            total_income+=200
        elif age<=40:
            total_income+=400
        else:
            total_income+=300
        patient_count+=1     
calculate_total_income()