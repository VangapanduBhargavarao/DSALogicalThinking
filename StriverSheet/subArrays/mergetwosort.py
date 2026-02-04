#### in the given one we have to merge the two sorted arrays.

def sort(nums1,nums2,n,m):
    i=n-1
    j=m-1
    idx=m+n-1
    while i>=0 and j>=0:
        if nums1[i]>=nums2[j]:
            nums1[idx]=nums1[i]
            idx-=1
            i-=1
        else:
            nums1[idx]=nums2[j]
            idx-=1
            j-=1
    while j>=0:
        nums1[idx]=nums2[j]
        idx-=1
        j-=1
    return nums1

m=int(input("enter the list2 size"))
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
print(f"After sorting the array is:{sort(nums1,nums2,len(nums1)-m,m)}")