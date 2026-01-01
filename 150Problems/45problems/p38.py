### find the average of the nubers
def find_average(nums):
    n=len(nums)
    sumi=0
    for val in nums:
        sumi+=val
    return sumi//n

nums=list(map(int,input().split()))
print(f"the average of given numbers is:{find_average(nums)}")
