#### find the largest element in the array.

def find_largest(nums):
    n=len(nums)
    maximum=float('-inf')
    for val in nums:
        if val>maximum:
            maximum=val
    return val

nums=list(map(int,input().split()))
print(f"The largest element in the given array is:{find_largest(nums)}")
