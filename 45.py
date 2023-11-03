def rev(string):
    if len(string)==1:
        return string[0]
    else:
        return string[-1]+rev(string[:-1])
s=input("enter a string")
s2=rev(s)
print("reverse is",s2)
