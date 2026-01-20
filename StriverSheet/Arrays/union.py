#### the below one is for the union of the two arrays.
### the below approach is the following the Map this is useful for the normal brute forcce.
"""
def union(A,B):
    freq=dict()
    for i in range(len(A)):
        freq[A[i]]=freq.get(A[i],0)+1
    for i in range(len(B)):
        freq[B[i]]=freq.get(B[i],0)+1
    union=sorted(freq.keys())
    return union
"""

### the below with the help of the set
"""
def union(A,B):
    union=set(A)|set(B)
    return sorted(union)"""

## for both set and map operations there is same time complexity that is O((m+n)log(m+n))

def union(A,B):
    pass

A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(union(A,B))