# s=input("enter a list of numbers seperated by space")
s="8,2,99,5,6,7,10,1,89,3"
num=list(map(int,s.split(",")))
for i in range(0,len(num)):
    if(i==0):
        print("strongest neighbour of",num[i],"is",num[i+1])
    elif(i==(len(num)-1)):
        print("strongest neighbour of",num[i],"is",num[i-1])
    else:
        if(num[i-1]>num[i+1]):
            print("strongest neighbour of",num[i],"is",num[i-1])
        else:
            print("strongest neighbour of",num[i],"is",num[i+1])
            
