### in this we have longest sub array with given sum k so here we have the positives and negitives and zero alos.

## this is the brute force approach.
def longest_subarray(nums,k):
    longest=0
    n=len(nums)
    for i in range(n):
        sumi=0
        for j in range(i,n):
            sumi+=nums[j]
            if sumi==k and (longest<j-i+1):
                longest=j-i+1
    return longest

nums=list(map(int,input().split()))
k=int(input())
print(f"the longest subarray is:{longest_subarray(nums,k)}")
