##### In this program we have to find the longest subarray with sum is equal to 0.

#### this one is for the finding length in brute force approach.
"""
def longest_subarray(nums):
    n=len(nums)
    maxlen=0
    for left in range(n):
        sumi=0
        for right in range(left,n):
            sumi+=nums[right]
            if sumi==0:
                maxlen=max(maxlen,right-left+1)
    return maxlen

#### here we given the subarray that is the maximum length of the sub array

def longest_sub(nums):
    n=len(nums)
    startpoint=endpoint=longest=0
    for left in range(n):
        sumi=0
        for right in range(left,n):
            sumi+=nums[right]
            if sumi==0 and longest<right-left+1:
                startpoint=left
                endpoint=right
                longest=right-left+1
    return nums[startpoint:endpoint+1]



nums=list(map(int,input().split()))
print(f"the subarray length is :{longest_subarray(nums)}")
print(f"The sub array is:{longest_sub(nums)}")
"""
#### ------------------------------ The above one is the Brute force approach -----------------

### optimal approach.
### optimal approach which pattern we have to follow.
"""
def long(nums):
    n=len(nums)
    seen=dict()
    sumi=maxlen=0
    for i in range(n):
        sumi+=nums[i]
        if sumi==0:
            maxlen=max(maxlen,i+1)
        rem=sumi-0
        if rem in seen:
            length=seen[rem]-i
            maxlen=max(maxlen,length)
        if sumi not in seen:
            seen[sumi]=i
    return maxlen
"""

def long(nums):
    maxlen=0
    sumi=0
    n=len(nums)
    seen=dict()
    for i in range(n):
        sumi+=nums[i]
        if sumi==0:
            maxlen=i+1
        else:
            if sumi in seen:
                length=i-seen[sumi]
                maxlen=max(maxlen,length)
            else:
                seen[sumi]=i
    return maxlen


nums=list(map(int,input().split()))
print(f"The lenght is:{long(nums)}")

