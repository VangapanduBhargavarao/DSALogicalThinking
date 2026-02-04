### this one is only focus on the normal checking but it behave the hazrad like the branching condition.
"""
def sort_colors(nums):
    n=len(nums)
    cntofzeros=cntofones=cntoftwos=0
    for val in nums:
        if val==0:
            cntofzeros+=1
        elif val==1:
            cntofones+=1
        else:
            cntoftwos+=1
    for i in range(n):
        if (cntofzeros):
            nums[i]=0
            cntofzeros-=1
        elif (cntofones):
            nums[i]=1
            cntofones-=1
        else:
            nums[i]=2
            cntoftwos-=1
    return nums
"""

#### the below one is the single pass with some algorithm.

def sort_colors(nums):
    n=len(nums)
    low=0
    high=n-1
    mid=0
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1    
        elif nums[mid]==1:
            mid+=1
        else:
            nums[high],nums[mid]=nums[mid],nums[high]
            high-=1
    return nums


nums=list(map(int,input().split()))
print(f"After sorting the array is:{sort_colors(nums)}")