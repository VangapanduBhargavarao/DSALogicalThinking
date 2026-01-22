### the given below function is find to the maximum consecutive function.

def max_consecutive(nums):
    count=0
    maxi=float('-inf')
    for val in nums:
        if val==1:
            count+=1
        else:
            count=0
        maxi=max(maxi,count)
    return maxi

nums=list(map(int,input().split()))
print(f"In the given arrray the maximum consetive ones are:{max_consecutive(nums)}")