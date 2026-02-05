### this is the classical binary search problem.
### one main thing keep it in the mind before applying the binary search that is nums is to be sorted always.
def binary_search(nums,target):
    n=len(nums)
    #left=0
    #right=n-1
    left,right=0,n-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1


nums=list(map(int,input().split()))
target=int(input())
print(f"The index found at the:{binary_search(nums,target)}")