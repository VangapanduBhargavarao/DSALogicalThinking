#### remove duplicates from the array.

### duplicate elements means the same element is not side by side mutiple times.
### repeated elements means the elements is not repeated in the total whole array.

def duplicate_array(nums):
    result=list()
    for val in nums:
        if val not in result:
            result.append(val)
    return result


nums=list(map(int,input().split()))
print(f"after remove duplicates array is:{duplicate_array(nums)}")

