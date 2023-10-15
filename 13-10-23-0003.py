#7 To print all colours from colours-list1 not contained in colours-list2
clr1=set(input("enter colours seperated by space ").split())
clr2=set(input("enter colours seperated by space ").split())
print(clr1-clr2)
#8 to merge 2 dictionaries
d1={"name":"ajai","batch":"mca","mark1":23}
d2={"mark2":56,"mark3":89}
d1.update(d2)
print(d1)

#9
print(sorted(d1.items(),reverse=True))

#10

