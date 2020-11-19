digit_list=[]
def large_number(num_string):
    try:
        num=int(num_string)
        temp=num
        while(temp>0):
            digit=temp%10
            temp=temp//10
            digit_list.append(temp%10)
        digit_list=digit_list.sort()
        print(digit_list)
    except ValueError:
         print("Wrong Values Entered")
    except NameError:
         print("Name not Defined")
    except ZeroDivisionError:
         print("Divided by Zero Error")
    except:
         print("Some Error Occured")
             
   
         

num_string=input("Enter a number:")
large_number(num_string)

        
        
        
        
        
        
    
