#### for the given problem we have to arrange the elements according to relative order
"""
def arrange(nums):
    positive=[]
    negitive=[]
    n=len(nums)
    for val in nums:
        if val%2==0:
            positive.append(val)
        else:
            negitive.append(val)
    for i in range(n//2):
        nums[2*i]=positive[i]
        nums[2*i+1]=negitive[i]
    return nums
"""

###### in the above problem we use the double pass but here we have to use the single pas solution.

def arrange(nums):
    n=len(nums)
    res=[0]*n
    posindex,negindex=0,1
    for i in range(n):
        if nums[i]>0:
            res[posindex]=nums[i]
            posindex+=2
        else:
            res[negindex]=nums[i]
            negindex+=2
    return res


nums=list(map(int,input().split()))
print(f"After arrange:{arrange(nums)}")