#### in the below problem we will count the no of subarrays with sum=k

### this is the brute force approach here time compplexity is more.
"""
def count_subarray(nums,k):
    n=len(nums)
    count=0
    for i in range(n):
        sumi=0
        for  j in range(i,n):
            sumi+=nums[j]
            if sumi==k:
                count+=1
    return count
"""

def count_subarray(nums,k):
    presum=dict()
    presum[0]=1
    count=sumi=0
    for i in range(len(nums)):
        sumi+=nums[i]
        rem=sumi-k
        count=count+presum.get(rem,0)
        presum[sumi]=presum.get(sumi,0)+1
    return count


nums=list(map(int,input().split()))
k=int(input())
print(f"the count of subarrays with sum K is:{count_subarray(nums,k)}")