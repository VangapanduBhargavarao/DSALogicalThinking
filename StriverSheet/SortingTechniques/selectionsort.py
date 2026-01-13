#### the selection sort is follows the main thing or every iteration the minimum element we have to keep at start
def selection_sort(nums):
    n=len(nums)
    for i in range(n):
        minindex=i
        for j in range(i,n):
            if nums[j]<nums[minindex]:
                minindex=j
        nums[i],nums[minindex]=nums[minindex],nums[i]
    return nums


nums=list(map(int,input().split()))
print(f"after sortign the array is:{selection_sort(nums)}")