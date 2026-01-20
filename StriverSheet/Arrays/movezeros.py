### move zeros to the end
## brute force approach here to follow the main thing is.
"""
def move_zeros(nums):
    n=len(nums)
    count=0
    result=[]
    for val in nums:
        if val==0:
            count+=1
        else:
            result.append(val)
    for i in range(count):
        result.append(0)
    return result
"""


def move_zeros(nums):
    n=len(nums)
    left=0
    for right in range(n):
        if nums[right]!=0:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
    return nums

nums=list(map(int,input().split()))
print(f"before array:{nums} and after array is:{move_zeros(nums)}")
