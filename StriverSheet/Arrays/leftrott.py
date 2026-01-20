### the below one is the brute force approach so we have to move to the optimal approach.
"""def rotate_left(nums):
    n=len(nums)
    result=[]
    for i in range(1,n):
        result.append(nums[i])
    result.append(nums[0])
    return result"""

def rotate_left(nums):
    n=len(nums)
    first=nums[0]
    for i in range(1,n):
        nums[i-1]=nums[i]
    nums[-1]=first
    return nums

nums=list(map(int,input().split()))
print(f"before rotate array is:{nums} after rotate array is:{rotate_left(nums)}")