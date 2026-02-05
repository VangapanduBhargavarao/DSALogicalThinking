#### here we have to find the search element in the given array.
### but the array is in the sorted and rotated so try to manipulate.

### this is the extreme brute force approach so try to reduce the time complexity.
"""
def search(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
"""

def search(nums,target):
    pass


nums=list(map(int,input().split()))
target=int(input())
print(f"the given one is :{search(nums,target)}")