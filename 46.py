#1) Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square.
import math
n=9999
#l=[i for i in range(1000,int(n)) if math.sqrt(int(n))%10==0 and int(n[0])%2==0 and int(n[1])%2==0 and int(n[2])%2==0 and int(n[3])%2==0 ]
l=list()
for i in range(1000,n):
    if(math.sqrt(i)==int(math.sqrt(i))):
        
        temp=str(i)
        if(int(temp[0])%2==0 and int(temp[1])%2==0 and int(temp[2])%2==0 and int(temp[3])%2==0 and temp[0]!="0" and temp[1]!="0" and temp[2]!="0" and temp[3]!="0" ):
            print(i)
            l.append(i)
print(l)
