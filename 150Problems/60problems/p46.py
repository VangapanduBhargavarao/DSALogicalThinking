### median in the given array.
nums=list(map(int,input().split()))
nums.sort()
n=len(nums)
if n%2!=0:
    print(f"the median of given array is:{nums[n//2]}")
else:
    median=(nums[n//2]+nums[n//2-1])//2
    print(f"for this values the median is the :{median}")

