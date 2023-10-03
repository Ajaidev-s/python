s1=input("enter colours seperated by commas")
# s1="red,black,blue,green"
colours=list(s1.split(','))
c=len(colours)
print(c)
print(colours[0:c:2])
