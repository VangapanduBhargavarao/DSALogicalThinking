## sum of the odd numbers in the given range
def sum_of_odd(start,end):
    sumi=0
    for val in range(start,end+1):
        if val%2!=0:
            sumi+=val
    return sumi
start=int(input())
end=int(input())
print(f"the odd numbers between the range is :{sum_of_odd(start,end)}")