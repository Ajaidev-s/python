#1,write a program to determine frequency of a word in a sentence
#2,write a program to determine frequency of alphabets in a word
#3,write a program to create an inverted dictionary

#2
s1=input("enter a word")
letter={}
for i in s1:
    letter[i]=letter.get(i,0)+1
print(letter)

#1
s2=input("enter a string").split()
words={}
for w in s2:
    words[w]=words.get(w,0)+1
print(words)

#3
student={"name":"Ajai","batch":"mca"}
inverse={}
inverse={v:k for k,v in student.items()}
#for key,value in student.items():
 #   inverse[value]=key
print(inverse)


