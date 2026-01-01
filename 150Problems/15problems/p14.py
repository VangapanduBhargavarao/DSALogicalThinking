# find the largest and smallest number
nums=list(map(int,input().split()))
largest=float('-inf')
smallest=float('inf')
n=len(nums)
for i in range(n):
    if nums[i]>largest:
        largest=nums[i]
    if nums[i]<smallest:
        smallest=nums[i]
print(f"the largest is :{largest} and the smallest is :{smallest}")