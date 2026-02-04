### here in the given problem we have to find the repeating and missing value.

### this is the extreme brute force approach we can think of that try to work on the another approach.
"""
def repeat(nums):
    n=len(nums)
    ans=[]
    seen=dict()
    nums.sort()
    repeat=missing=0
    val=1
    for num in nums:
        if val!=num:
            missing=val
            break
        val+=1
    for num in nums:
        seen[num]=seen.get(num,0)+1
    for k,v in seen.items():
        if v==2:
            repeat=k
    ans.append(repeat)
    ans.append(missing)
    return ans
    
"""

### the above one is the fully brute force approach so we have to find the different type of the solution.

def repeat(nums):
    n=len(nums)
    Sn=(n*(n+1))//2
    S2n=(n*(n+1)*(2*n+1))//6
    S=S2=0
    for i in range(n):
        S+=nums[i]
        S2+=nums[i]*nums[i]
    val1=S-Sn
    val2=S2-S2n
    val2=val2//val1
    x=(val1+val2)//2
    y=x-val1
    return [x,y]


nums=list(map(int,input().split()))
print(f"In the given array after these are:{repeat(nums)}")        