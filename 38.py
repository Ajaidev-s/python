def counting(list1):
    i=0
    for j in list1:
        if(len(j)>=2 and j[0]==j[-1]):
            i+=1
    print("count=",i)
s=input("Enter the setence")
s=s.split()
counting(s)
