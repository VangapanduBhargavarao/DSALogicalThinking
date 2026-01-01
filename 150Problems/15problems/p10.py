# conversion of the temparture
def conversion(C):
    F=(C*9/5)+32
    return F
C=int(input())
print(f"the conversion is :{conversion(C)}")
