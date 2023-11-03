def sum_digit(n):
    if n//10==0:
        return n
    else:
        return n%10+sum_digit(n//10)
n=int(input("enter the number"))
summ=sum_digit(n)
print("sum=",summ)
