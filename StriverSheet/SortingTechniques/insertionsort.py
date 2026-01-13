### insertion sort is works on the go through some element and from uptothose element make everything will be sorted.
def insertionsort(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums
        

nums=list(map(int,input().split()))
print(f"After sorting the array is:{insertionsort(nums)}")
