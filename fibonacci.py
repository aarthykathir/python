def getfib(N):
    if N==1:
        return 0
    if N<=3:
        return 1

    return getfib(N-1)+getfib(N-2)

N=int(input("Enter the Term for fibonacci series:"))

print(getfib(N))

def getfib1(N):
    if(N<1):
        print("Invalid")
        return
    elif(N==1):
        print(0)
        return
    elif(N==2):
        print(0,end=",")
        print(1)
        return
    a=0
    b=1
    print(a,end=",")
    print(b,end=",")
    n=2
    while(1):
        c=a+b
        a=b
        b=c
        n+=1
        if(n==N):
            print(c)
            return
        else:
            print(c, end=",")


getfib1(N)

def getfib1(N):
    if N==1:
        return 0
    elif(N<=3):
        return 1
    else:
        a=0
        b=1
        n=2
        while(1):
            c=a+b
            a=b
            b=c
            n+=1
            if(n==N):
                return c

print(getfib1(N))



