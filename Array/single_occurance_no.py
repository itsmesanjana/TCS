from collections import Counter
def single_occurance_no(arr):
    freq=Counter(arr)
    for key,val in freq.items():
        if val==1:
            return key
        
        
arr=[1,2,3,4,4,4,4,1,1,3,4,3]
print(single_occurance_no(arr))