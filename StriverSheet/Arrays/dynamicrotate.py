## the below version focus on the only the brute force approach.
"""def dynamic_rotate(nums,k,pos):
    n=len(nums)
    result=[]
    if n==0:
        return nums
    k=k%n
    if pos=="right":
        for i in range(n-k,n):
            result.append(nums[i])
        for i in range(0,n-k):
            result.append(nums[i])
    return result"""
    
def rotate_array(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    


### the below version is for optimized version
def dynamic_rotate(nums,k,pos):
    n=len(nums)
    if n==0 or k==0:
        return nums
    k=k%n
    if pos=="right":
        rotate_array(nums,0,n-1)
        rotate_array(nums,0,k-1)
        rotate_array(nums,k,n-1)
    elif pos=="left":
        rotate_array(nums,0,n-1)
        rotate_array(nums,0,n-k-1)
        rotate_array(nums,n-k,n-1)

    return nums

nums=list(map(int,input().split()))
k=int(input("enter"))
pos=input()
print(f"before rotate:{nums} and after rotate is:{dynamic_rotate(nums,k,pos)}")