
### the below one is the brute force approch like what is given in problem statement we write it.
"""
def maxproduct(nums):
    maxproduct=float('-inf')
    n=len(nums)
    for i in range(n):
        product=1
        for j in range(i,n):
            product*=nums[j]
            maxproduct=max(maxproduct,product)
    return maxproduct
"""


#### the below one is the optimal approach for this problem.
## the optimal approach is the main problem we have to find the prefix and suffix ones.

def maxproduct(nums):
    n=len(nums)
    ans=float('-inf')
    pre=suff=1
    for i in range(n):
        if pre==0:pre=1
        if suff==0:suff=1
        pre*=nums[i]
        suff*=nums[n-i-1]
        ans=max(ans,max(pre,suff))
    return ans



nums=list(map(int,input().split()))
print(f"the maximum produt is:{maxproduct(nums)}")