#4
num1=input("enter list of numbers ")
num2=input("enter the list of number")
num1=list(map(int,num1.split()))
num2=list(map(int,num2.split()))
print("they are of same length : ",len(num1)==len(num2))
print("Is there sums are same: ",sum(num1)==sum(num2))
print("they have common elements:",bool(len(set(num1)&set(num2))))

#5
# To write a python program to add 'ing' at the end of the string.if already ends with 'ing' then add 'ly'
s1=input("enter a string")
s1 += 'ly' if s1.endswith('ing') else 'ing'
print(s1)

#6 to accept a string and return the length of longest word if the result has more than one word ,then print bingo
words=input("enter the string").split()
words.sort(key=len,reverse=True)
print("max length=",len(words[0]))
if(len(words[0])==len(words[1])):
    print("bingo")

