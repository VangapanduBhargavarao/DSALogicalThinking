### the longest subarray with the given sum k

### here we return the length of the longest sub array it equals to sum K.
"""
def longest_subarray(nums,k):
    n=len(nums)
    longest=sumi=0
    maxi=float('-inf')
    for i in range(n):
        sumi=0
        for j in range(i,n):
            sumi+=nums[j]
            if sumi==k:
                longest=max(longest,j-i+1)
    return longest
"""


### here we return the subarray which is the longest subarray with the sum equals to K.
"""
def subarray(nums,k):
    n=len(nums)
    longest=sum=ansstart=ansend=0
    maxi=float('-inf')
    for i in range(n):
        sumi=0
        for j in range(i,n):
            sumi+=nums[j]
            if sumi==k and j-i+1>longest:
                ansstart=i
                ansend=j
    return nums[ansstart:ansend+1]
"""


###### the below is the optimal approach for the above approach 
### here we only return the length of longest subarray maximum value.
## This approach is the sliding window+ two pointers approach .


def longest_subarray(nums,k):
    n=len(nums)
    left=right=longest=0
    sumi=nums[0]
    while right<n:
        while left<=right and sumi>k:
            sumi=sumi-nums[left]
            left+=1
        if sumi==k:
            longest=max(longest,right-left+1)
        right+=1
        if right<n:
            sumi+=nums[right]
            
    return longest

## we return the subarray.
### here we use the sliding window+ two pointers approach to solve the problem.
def subarray(nums,k):
    n=len(nums)
    left=right=longest=ansstart=ansend=0
    sumi=nums[0]
    while right<n:
        while left<=right and sumi>k:
            sumi-=nums[left]
            left+=1
        if sumi==k and (right-left+1>longest):
            longest=(right-left+1)
            ansstart=left
            ansend=right
        right+=1
        if right<n:
            sumi+=nums[right]
    return nums[ansstart:ansend+1]

nums=list(map(int,input().split()))
k=int(input())
print(f"The longest subarray is length is:{longest_subarray(nums,k)}")
print(f"the subaarray is:{subarray(nums,k)}")
