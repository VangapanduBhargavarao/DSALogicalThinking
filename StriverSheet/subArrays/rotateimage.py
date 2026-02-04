def Reverse(nums):
    low=0
    high=len(nums)-1
    while low<high:
        nums[low],nums[high]=nums[high],nums[low]
        low+=1
        high-=1
def rotate_image(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for row in matrix:
        Reverse(row)
    return matrix

matrix=[]
while True:
    row=input()
    if row=="":
        break
    matrix.append(list(map(int,row.split())))
matrix=rotate_image(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j],end=" ")
    print()
