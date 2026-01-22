### the below function is used to find the value that is repeated only single time.
"""def single_number(nums):
    seen=dict()
    for val in nums:
        seen[val]=seen.get(val,0)+1
    for key,val in seen.items():
        if val==1:
            return key"""


#### the below one is the optimized approach for the finding the single number.
def single_number(nums):
    """
    Docstring for single_number
    
    :param nums: this validates only when the every number expect twwice otherwise it is not possible.
    """
    ans=0
    for val in nums:
        ans=ans^val
    return ans
    

nums=list(map(int,input().split()))
print(f"The number is repeated single time is:{single_number(nums)}")