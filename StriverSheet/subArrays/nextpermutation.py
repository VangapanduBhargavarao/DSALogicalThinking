#### next permutation in the  given arrays.
def Reverse(nums,low,high):
    while low<high:
        nums[low],nums[high]=nums[high],nums[low]
        low+=1
        high-=1
    return nums

def next_permutation(nums):
    n=len(nums)
    ind=-1
    for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            ind=i
            break
    if ind==-1:
        return Reverse(nums,0,n-1)
    for i in range(n-1,ind,-1):
        if nums[i]>nums[ind]:
            nums[i],nums[ind]=nums[ind],nums[i]
            break
    return Reverse(nums,ind+1,n-1)


nums=list(map(int,input().split()))
print(f"next permutation is:{next_permutation(nums)}")