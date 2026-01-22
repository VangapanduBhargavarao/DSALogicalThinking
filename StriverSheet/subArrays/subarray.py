#### return the subarray that is the maximum sum.
### the below is the brute force approach to find the subarry
"""
def subarray(nums):
    n=len(nums)
    result=[]
    maxi=float('-inf')
    ansstart=ansend=0
    for i in range(n):
        sumi=0
       
        for j in range(i,n):
            sumi=sumi+nums[j]
            if sumi>maxi:
                maxi=sumi
                ansstart=i
                ansend=j
    for i in range(ansstart,ansend+1):
        result.append(nums[i])
    return result
"""


########## the below is the optimal approach 
def subarray(nums):
    maxi=float('-inf')
    sumi=start=ansstart=ansend=0
    n=len(nums)
    for i in range(n):
        if sumi==0:
            start=i
        sumi+=nums[i]
        if sumi>maxi:
            maxi=sumi
            ansstart=start
            ansend=i
        if sumi<0:
            sumi=0
    return nums[ansstart:ansend+1] 
nums=list(map(int,input().split()))
print(subarray(nums))