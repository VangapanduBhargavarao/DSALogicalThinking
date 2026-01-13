### Recusrive bubbleSort is work on the some things like how it works 

def bubble_sort(nums,n):
    if n==1:
        return 
    for j in range(n-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
    bubble_sort(nums,n-1)
    #return nums

nums=list(map(int,input().split()))
print(f"before Swapping is :{nums}")
bubble_sort(nums,len(nums))
print(f'After Sorting is:{nums}')