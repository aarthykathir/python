prime_list=[]
for i in range(2,100):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        prime_list.append(i)
    

print(prime_list)
        
