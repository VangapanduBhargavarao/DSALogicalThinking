### create the matrix grid for these values.
size=int(input())
final_grid=size*size
result=[]
for i in range(1,final_grid+1):
    result.append(i)
print(f"For given size values are:{result}")