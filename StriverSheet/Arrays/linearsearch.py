def linear_search(nums,val):
    n=len(nums)
    for i in range(n):
        if nums[i]==val:
            return i
    return -1

nums=list(map(int,input().split()))
val=int(input())
print(f"The element is present at:{linear_search(nums,val)} at index")