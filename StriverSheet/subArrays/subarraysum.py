#### in the below given the subaraay find the maximum subarray.

#### brute force.
"""
def max_subarray(nums):
    n=len(nums)
    maxi=float('-inf')
    for i in range(n):
        sumi=0
        for j in range(i,n):
            sumi+=nums[j]
            maxi=max(maxi,sumi)
    return maxi
"""

#### the below one is the optima approach for finding the solution

def max_subarray(nums):
    maxi=float('-inf')
    sumi=0
    for val in nums:
        sumi+=val
        maxi=max(maxi,sumi)
        if sumi<0:
            sumi=0
    return maxi



nums=list(map(int,input().split()))
print(f"for given the array maximum sub array is:{max_subarray(nums)}")