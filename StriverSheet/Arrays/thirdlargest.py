#### print the third largest element in the given array.
def third_largest(nums):
    first=second=third=float('-inf')
    for val in nums:
        if val>first:
            third=second
            second=first
            first=val
        elif val!=first and val>second:
            third=second
            second=val
        elif val!=first and val!=second and val>third:
            third=val
    return third

nums=list(map(int,input().split()))
print(f"The given elements in the third is:{third_largest(nums)}")