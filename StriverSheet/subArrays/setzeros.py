#### here we have to set the zeros in the given matrix




#### this is the optimal approach for the place the values based on the given matrix.

## we use the external data structure so here this one will help full for our data.


def set_zeros(nums):
    rows=len(nums)
    cols=len(nums[0])
    row=[0]*rows
    col=[0]*cols
    for i in range(rows):
        for j in range(cols):
            if nums[i][j]==0:
                row[i]=1
                col[j]=1
    for i in range(rows):
        for j in range(cols):
            if row[i]==1 or col[j]==1:
                nums[i][j]=0
    return nums


matrix=[]
while True:
    row=input()
    if row=="":
        break
    matrix.append(list(map(int,row.split())))
print(f"the matrix before zeros:{matrix}")
print("----------------")
print(f"After the matrix is:{set_zeros(matrix)}")