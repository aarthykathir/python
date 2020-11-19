def sum():
    num=int(input("Enter a number to find its sum of digits:"))
    sum_of_digits=0
    temp=num
    while(temp>0):
        digit=temp%10
        temp=temp//10
        sum_of_digits=sum_of_digits+digit
    return sum_of_digits


result=sum()
print("The sum of digits are:",result)

        
