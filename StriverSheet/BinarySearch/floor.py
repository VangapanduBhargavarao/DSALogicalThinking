#### this problem we have to find the floor and ceil of the given array.

### this is the exterme brute force approach for the given problem.
"""
def find(nums,x):
    n=len(nums)
    floor=ceil=n
    for i in range(n):
        if nums[i]==x:
            floor=x
            break
        elif nums[i]>x:
            floor=nums[i-1]
            break
    for i in range(n):
        if nums[i]==x:
            ceil=x
            break
        elif nums[i]>x:
            ceil=nums[i]
            break
    return [floor,ceil]
"""

#### the below is the optimal approaches for the find the floor and ceil of the given code.

def findfloor(nums,x):
    n=len(nums)
    left,right=0,n-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]<=x:
            ans=nums[mid]
            left=mid+1
        else:
            right=mid-1
    return ans

def findceil(nums,x):
    n=len(nums)
    left,right=0,n-1
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]>=x:
            ans=nums[mid]
            right=mid-1
        else:
            left=mid+1
    return ans
    
def find(nums,x):
    floor=findfloor(nums,x)
    ceil=findceil(nums,x)
    return [floor,ceil]



nums=list(map(int,input().split()))
target=int(input())
print(f"the floor and ceil are:{find(nums,target)}")