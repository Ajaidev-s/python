
def even(list1):
    for i in list1:
        if(237==i):
            break
        elif not i%2:
            print(i)
n=input("enter collection of integers:")
n=list(map(int,n.split()))
even(n)
        
