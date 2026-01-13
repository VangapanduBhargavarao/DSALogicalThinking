### bubble sort is the technique for every iteraction we have to push the maximum element to the last of the array.
def bubble_sort(nums):
    n=len(nums)
    for i in range(n-1):
        for j in range(n-1-i):
            if nums[j+1]<nums[j]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

nums=list(map(int,input().split()))
print(f"before sorting array is:{nums} then after sortring is:{bubble_sort(nums)}")