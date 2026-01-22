### find the majority element in the given array

def find_majority(nums):
    count=el=0
    n=len(nums)
    for val in nums:
        if count==0:
            el=val
        if val==el:
            count+=1
        else:
            count-=1
    cnt=nums.count(el)
    if cnt>(n//2):
        return el
    

nums=list(map(int,input().split()))
print(f"The majority element is:{find_majority(nums)}")