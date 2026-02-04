### [1,2,3,0,4,0,6,0,0,5,0,7]

def move_zeros(nums):
    n=len(nums)
    result=[]
    cntofzeros=0
    for val in nums:
        if val!=0:
            result.append(val)
        else:
            cntofzeros+=1
    for _ in range(cntofzeros):
        result.append(0)
    return result


### optima approach
[1,2,3,0,4,0,6,0,0,5,0,7]
def move(nums):
    n=len(nums)
    left=0
    for right in range(n):
        if nums[right]!=0:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
    return nums

     

nums=list(map(int,input().split()))
print(f"After:{move_zeros(nums)}")
print(f"After:{move(nums)}")


70 20 30 50 60 10 40 
70 20 30 --> 70 ,20 30 ---> 20 30 
50 60 10 40 

## 70 20 30 50 60 10 40 
   70 20 30      50 60 10 40 ---> 10 40 50 60 
   70  20 30        50 60  10 40 
        20 30 50 60  10 40 

