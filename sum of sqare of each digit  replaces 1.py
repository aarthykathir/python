def find_happy(num):
    count=0
    m=0
    result="Unhappy number"
    while(m==0 and count<10):
        sum_of_digits=0
        while(num>0):
            digit=num%10
            num=num//10
            sum_of_digits=sum_of_digits+digit**2        
        if(sum_of_digits==1):
            result="Happy Number"
            m=m+1
        elif(sum_of_digits>9):
            num=sum_of_digits
            count=count+1
        elif(sum_of_digits!=1 and sum_of_digits<10):    
            result="Unhappy Number"
            m=m+1
    return result


value=int(input("Enter a number:"))
ans=find_happy(value)
print("Given Number is an ",ans)
        
