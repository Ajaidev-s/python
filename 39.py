#a
large=lambda a,b : print(a) if a>b else print(b)
large(5,9)
#b
large=lambda a:print(not a%5)
large(5)
large(6)
#c

s=input("enter words")
l=list(filter(lambda x:len(x)>5,s.split()))
print(l)
#d
num=input("enter the numbers seperated by spaces")
num=list(map(int,num.split()))
l2=list(map(lambda x:(x+.1*x) if x>1000 else (x+0.05*x),num))
print(l2)
