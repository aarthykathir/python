def product():
    num=int(input("Enter a number to find its product of digits:"))
    product_of_digits=1
    temp=num
    while(temp>0):
        digit=temp%10
        temp=temp//10
        product_of_digits=product_of_digits*digit
    return product_of_digits


result=product()
print("The product of digits are:",result)
