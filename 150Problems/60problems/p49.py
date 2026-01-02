### second largest number in the array.
nums=list(map(int,input().split()))
maximum=secondmaximum=float('-inf')
for val in nums:
    if val>maximum:
        secondmaximum=maximum
        maximum=val
    elif val!=maximum and val>secondmaximum:
        secondmaximum=val
print(f"In the given array the second maximum element is:{secondmaximum}")