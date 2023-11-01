def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number"))
factt=fact(n)
print("factorial of",n,"is",factt)
    
