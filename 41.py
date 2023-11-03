def sum_list(l):
    if(len(l)==0):
        return 0
    else:
        return l[0]+sum_list(l[1:])

n=list(map(int,input("enter the number").split()))
summ=sum_list(n)
print("sum =",summ)
