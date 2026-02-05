##### this is the upper bound because in this upper bound.
### in this upper bound we have to find the element position where it is the some greater.
### This is the Brute force approach.

"""
def upper_bound(nums,x):
    n=len(nums)
    for i in range(n):
        if nums[i]>x:
            return i
    return n
"""

def upper_bound(nums,x):
    n=len(nums)
    left,right=0,n-1
    ans=len(nums)
    while left<=right:
        mid=(left+right)//2
        if nums[mid]>x:
            ans=mid
            right=mid-1
        else:
            left=mid+1
    return ans



nums=list(map(int,input().split()))
x=int(input())
print(f"the given upper bound value is:{upper_bound(nums,x)}")