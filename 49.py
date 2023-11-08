#  Accept a sentence from user and display the total count of vowels in the sentence.
#s=input("enter a string")
s="hello my friend"
count=0
vowel={"a","A",'e','E','i','I','o','O','u','U'}
for i in s:
    if(i in vowel):
        count+=1
print("number of vowels is",count)