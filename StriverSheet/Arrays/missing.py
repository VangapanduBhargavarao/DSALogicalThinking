### find the missing number in the given array.
def find_miss(nums):
    n=len(nums)
    duplicate_sum=0
    for val in nums:
        duplicate_sum+=val
    actual_sum=(n*(n+1))//2
    return actual_sum-duplicate_sum

nums=list(map(int,input().split()))
print(f"The missing number in the given nums is:{find_miss(nums)}")