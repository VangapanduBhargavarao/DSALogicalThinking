#### Brute Force approach for the merge intervals.
## here we follow the approach like the how to decode like the start and end.
### the underlying pattern is the two pointers approach so we can follow that one.
"""
def merge_intervals(nums):
    ans=[]
    nums.sort()
    n=len(nums)
    for i in range(n):
        start=nums[i][0]
        end=nums[i][1]
        if ans and nums[i][0]<ans[-1][1]:
            continue
        for j in range(i+1,n):
            if end>=nums[j][0]:
                end=max(end,nums[j][1])
        ans.append([start,end])
    return ans
"""
#### this is the optimal approach for the finding the merge intervals.
## in this main thing about the how we have to handle the values.

def merge_intervals(nums):
    n=len(nums)
    ans=[]
    for i in range(n):
        if not ans or nums[i][0]>ans[-1][1]:
            ans.append(nums[i])
        else:
            ans[-1][1]=max(ans[-1][1],nums[i][1])
    return ans




nums=[]
while True:
    row=input()
    if row=="":
        break
    else:
        nums.append(list(map(int,row.split())))

print(f"The merge intervals after operations:{merge_intervals(nums)}")