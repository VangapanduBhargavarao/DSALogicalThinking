#### the problem is to find the minimum diffeence pairs that are having minimum difference.


def leet(nums):
    n=len(nums)
    mindiff=float('inf')
    nums.sort()
    result=[]
    for i in range(n-1):
        diff=nums[i+1]-nums[i]
        mindiff=min(diff,mindiff)
    for i in range(n-1):
        if nums[i+1]-nums[i]==mindiff:
            result.append([nums[i],nums[i+1]])
    return result


nums=list(map(int,input().split()))
print(f"The list of arrays are:{leet(nums)}")