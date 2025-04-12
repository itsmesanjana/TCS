from collections import Counter

def single_count_element(arr):
    freq=Counter(arr)
    for key,val in freq.items():
        if val==1:
            return key


arr=[1,1,1,2,2,2,3,4,4,5,5]
print(single_count_element(arr))