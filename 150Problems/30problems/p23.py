## count the number of digits in the number
def count_number_of_digits(num):
    count=0
    while num!=0:
        count+=1
        num//=10
    return count
num=int(input())
print(f"the number of digits contain number is:{count_number_of_digits(num)}")