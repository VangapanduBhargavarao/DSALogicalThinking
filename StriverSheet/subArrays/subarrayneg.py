### in this we have longest sub array with given sum k so here we have the positives and negitives and zero alos.

## this is the brute force approach.
"""
def longest_subarray(nums,k):
    longest=0
    n=len(nums)
    for i in range(n):
        sumi=0
        for j in range(i,n):
            sumi+=nums[j]
            if sumi==k and (longest<j-i+1):
                longest=j-i+1
    return longest
"""


#### this approach is the optimal one for the if the array have the +ves and negitives and zeros.
def longest_subarray(nums,k):
    n=len(nums)
    seen=dict()
    sumi=0
    maxlen=0
    for i in range(n):
        sumi+=nums[i]
        if sumi==k:
            maxlen=max(maxlen,i+1)
        rem=sumi-k
        if rem in seen:
            length=i-seen[rem]
            maxlen=max(maxlen,length)
        if sumi not in seen:
            seen[sumi]=i
    return maxlen


nums=list(map(int,input().split()))
k=int(input())
print(f"the longest subarray is:{longest_subarray(nums,k)}")
