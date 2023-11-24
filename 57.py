import os
op=open("paragragh.txt","r")
ls=op.read().split()
ls.sort(key=len,reverse=True)
length=len(ls[0]);
print("the maximum length of word is ",length,"\n The words having maximum length are:")
[print(x) for x in ls if len(x)==length]
op.close()
