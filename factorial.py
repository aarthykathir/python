def find_factorial(number):
    factorial=1
    while(number>0):
        factorial=factorial*number
        number=number-1
    return factorial
number=int(input("Enter a number to find factorial:"))
result=find_factorial(number)
print("Factorial of ",number,"is :",result)
        
        
    
