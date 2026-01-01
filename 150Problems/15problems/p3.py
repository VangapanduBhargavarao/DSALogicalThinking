# write a program to Leap year

year=int(input())
if year%4==0 and year%100!=0:
    print("leap year")
elif year%100==0 and year%400!=0:
    print("Not a leap year")
elif year%400==0:
    print("leap year")
else:
    print("not leap year")