#### this is for the insert in the postion
"""
def insert(nums,target):
    n=len(nums)
    for i in range(n):
        if nums[i]>=target:
            return i
    return n
"""


#### this is the optimal approa
def insert(nums,target):
    n=len(nums)
    left,right=0,n-1
    ans=len(nums)
    while left<=right:
        mid=(left+right)//2
        if nums[mid]>=target:
            ans=mid
            right=mid-1
        else:
            left=mid+1
    return ans


nums=list(map(int,input().split()))
target=int(input())
print(f"the insert position is:{insert(nums,target)}")