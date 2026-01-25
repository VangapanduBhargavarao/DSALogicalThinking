### here we have to find the longest consecutive elements in the array.
"""
def longest_consecutive(nums):
    n=len(nums)
    longest=0
    for i in range(n):
        val=nums[i]
        count=1
        val+=1
        while val in nums:
            count+=1
            val=val+1
        longest=max(longest,count)
    return longest
"""

#### the below one is the better approach with the help of the sorting of the array and find the values.
"""

def longest_consecutive(nums):
    nums.sort()
    n=len(nums)
    cnt=0
    longest=1
    last_smaller=float('-inf')
    for i in range(n):
        if nums[i]-1==last_smaller:
            cnt+=1
            last_smaller=nums[i]
        elif nums[i]!=last_smaller:
            cnt=1
            last_smaller=nums[i]
        longest=max(longest,cnt)
    return longest
"""

#### optimal approach for the above poblem

def longest_consecutive(nums):
    n=len(nums)
    if n==0:
        return 0
    longest=1
    st=set()
    for val in nums:
        st.add(val)
    for it in st:
        if it-1 not in st:
            cnt=1
            x=it
            while x+1 in st:
                cnt+=1
                x=x+1
            longest=max(longest,cnt)
    return longest


nums=list(map(int,input().split()))
print(f"the longest consecutive is:{longest_consecutive(nums)}")