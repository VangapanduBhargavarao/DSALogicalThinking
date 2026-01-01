### find the missing numbers in the given sequence
def find_maximum(sequence):
    max_value=float('-inf')
    for val in sequence:
        if val>max_value:
            max_value=val
    return max_value

def find_missing(sequence: list[int])->list:
    maxium=find_maximum(sequence)
    missing=[]
    for i in range(1,maxium+1):
        if i not in sequence:
            missing.append(i)
    return missing

sequence=list(map(int,input().split()))
print(f"In the given range the missing numbers are:{find_missing(sequence)}")


## for the above optimized verion in the place of list convert into set 
## beacuse in the set best and average case are TC is O(1) for find the values.
## so that is optimized version without using any extra operations.
