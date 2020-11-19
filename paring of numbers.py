n,k,y=input("Enter three number with space between them:").split(" ") 
n=int(n);k=int(k)
b=[]
print("y:",y)
for i in range(4):
    c=int(input("Enter a number:"))
    b.append(c)
z=[]
for i in b:
    if(i>k):
        continue
    x=k-i
    if i in z or x in z:
        continue
    if x in b:
        z.append(x)
        print("The Pairs are:",i,x)
        
