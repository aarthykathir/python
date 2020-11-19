def armstrong(num):
    sum_of_digits=0
    temp=num
    while(temp>0):
        digit=temp%10
        temp=temp//10
        sum_of_digits=sum_of_digits+digit**3
    return sum_of_digits


num=int(input("Enter a number to check whether it is an amrstrong number:"))
result=armstrong(num)
if(result==num):
    print("The given number ",num," is an armstrong number")
else:
    print("The given number ",num," is not an armstrong number")

