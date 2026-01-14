#### second largest element in the given array
def second_largest(nums):
    first=second=float('-inf')
    for val in nums:
        if val>first:
            second=first
            first=val
        elif val>second and val!=first:
            second=val
    return second


nums=list(map(int,input().split()))
print(f"The second largest element is:{second_largest(nums)}")