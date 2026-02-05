### in this problem we have to find the lower bound of the problem.
### lower bound means in the which location we have to keep the elment in the given array.

#### this is the classical linear search problem here we have to minimize time complexity.

"""
def lower_bound(nums,x):
    n=len(nums)
    for i in range(n):
        if nums[i]>=x:
            return i
    return n+1
"""

def lower_bound(nums,x):
    n=len(nums)
    left,right=0,n-1
    ans=len(nums)
    while left<=right:
        mid=(left+right)//2
        if nums[mid]>=x:
            ans=mid
            right=mid-1
        else:
            left=mid+1
    return ans

nums=list(map(int,input().split()))
x=int(input())
print(f"the main insert position is:{lower_bound(nums,x)}")