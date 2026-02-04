#### here we have to find the number of subarrays have the xor is equal to the K

def count_xor(nums,target):
    n=len(nums)
    count=0
    for i in range(n):
        xor=0
        for j in range(i,n):
            xor^=nums[j]
            if xor==target:
                count+=1
    return count



###### this one is for the return the sub arrays also.

def subarrays(nums,target):
    n=len(nums)
    ans=[]
    for i in range(n):
        xor=0
        for j in range(i,n):
            xor^=nums[j]
            if xor==target:
                ans.append(nums[i:j+1])
    return ans

nums=list(map(int,input().split()))
target=int(input())
print(f"The number of sub arrays are:{count_xor(nums,target)}")
print(f"The sub arrays are:{subarrays(nums,target)}")