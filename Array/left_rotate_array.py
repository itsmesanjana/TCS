def left_rotate_array(nums,k):
    n=len(nums)
    k%=n
    # return nums[k:]+nums[:k]
    def reverse_arr(start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
    reverse_arr(0,k-1)
    reverse_arr(k,n-1)
    reverse_arr(0,n-1)
    
    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(left_rotate_array(nums, k))