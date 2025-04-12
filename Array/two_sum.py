def two_sum(nums,target):
    num_map={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in num_map:
            return[num_map[complement],i]
        num_map[num]=i
    return []

target=7
nums=[1,2,3,4]
print(two_sum(nums,target)) 