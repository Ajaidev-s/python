#6) Write a program to search an item in a given list and display the number of occurrences of the given item.
l=list(map(int,input("enter the numbers seperated by space").split()))
print(l)
s1={}
for i in l:
    s1[i]=s1.get(i,0)+1
print(s1)
num=int(input("enter the element to search"))
print(num,"appears",s1[num],"times")

