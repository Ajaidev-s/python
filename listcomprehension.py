#creating a list
# a=[1,2,3,4,5,0,-1,-5,-8,-99,-78]
print("part a")
a=input("Enter numbers seperated by commas")
a=list(map(int,a.split(',')))
print(a)
#code to extract possitive number from a list of numbers(a)
pos=[item for item in a if(item>0)]
print(pos)
print("part b")
#code to create a list by taking square of element from a given list(b)
sqr=[item**2 for item in a ]
print(sqr)
#checking vowels(c)
print("part c")
vowels=['a','A','e','E','i','I','o','O','u','U']
s1=input("enter a string")
# s1="hello my name is ajai,(with an i offcourse)"
s2=list(s1)
print(s2)
v1=[item for item in s2 if(item in vowels)]
print("vowels: ",v1)
#removing even  numbers from a given list(d)
noteven=[item for item in a if(item%2==1 or item<=0)]
print("Not even: ",noteven)
#leap years in a range 2023 to year(f)
year=int(input("enter year"))
# year=2500
leap=[i for i in range(2023,year) if((i%400==0) or(i%100 !=0) and (i%4==0))]
print("leap years:",leap)
