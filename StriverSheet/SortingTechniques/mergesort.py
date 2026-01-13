### Merge sort is also one sorting technique which follows the one algorithm.
### Divde and Conuquer it follows the divide and conuer idea and based on that idea we can simply implement this.
def merge(nums,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while left<=mid and right<=high:
        if nums[left]<=nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1
    while left<=mid:
        temp.append(nums[left])
        left+=1
    while right<=high:
        temp.append(nums[right])
        right+=1
    for i in range(low,high+1):
        nums[i]=temp[i-low]

def merge_sort(nums,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    merge_sort(nums,low,mid)
    merge_sort(nums,mid+1,high)
    merge(nums,low,mid,high)
    return nums
    

nums=list(map(int,input().split()))
print(f"After Sorting the array:{merge_sort(nums,0,len(nums))}")


### Overall time complextity for the mergesort is O(NlogN)