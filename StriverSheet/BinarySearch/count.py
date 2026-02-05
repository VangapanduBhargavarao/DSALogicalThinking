##### here we have to find the count the occurrences of the given number.

#### this is the brute force approach we have to follow the order.
"""
def count(nums,target):
    count=0
    for val in nums:
        if val==target:
            count+=1
    return count
"""
def count(nums,target):
    pass


nums=list(map(int,input().split()))
target=int(input())
print(f"the number of times it repeats is:{count(nums,target)}")