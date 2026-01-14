#### check the given array is sorted or not

def check_sort(nums):
    n=len(nums)
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            return  False
    return True


nums=list(map(int,input().split()))
print(f"The given array is sorted or not:{check_sort(nums)}")