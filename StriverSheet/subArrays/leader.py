#### here we have to find the leaders in the given array so the leaders are the.
### if we stand at one element then the all elements left side are equal or low elements.

## the below one time complexity is O(n^2)
### space complexity is O(N) but it is only for returning the values.
"""

def leaders_array(nums):
    n=len(nums)
    res=[]
    for i in range(n):
        leader=True
        for j in range(i+1,n):
            if nums[j]>=nums[i]:
                leader=False
                break
        if leader:
            res.append(nums[i])
    return res
"""

### the below one is the for the find leaders but in the optimal version.

def leaders_array(nums):
    n=len(nums)
    res=[]
    leader=nums[-1]
    res.append(leader)
    for i in range(n-2,-1,-1):
        if nums[i]>leader:
            leader=nums[i]
            res.insert(0,leader)
    return res

nums=list(map(int,input().split()))
print(f"For given array the leaders are the :{leaders_array(nums)}")