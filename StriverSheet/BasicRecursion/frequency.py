#### count the frequency of each elements in the hashamp\

def count(nums):
    seen=dict()
    for val in nums:
        seen[val]=seen.get(val,0)+1
    return seen

nums=list(map(int,input().split()))
result=count(nums)
for key,val in result.items():
    print(f"the value :{key} repeats:{val} times")