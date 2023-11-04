l=list(map(int,input("enter perfentage of subject physics  maths chemistry respectivly seperated by space").split()))
fail=0
if(len(l)==3):
    marks={"physics":l[0],"Maths":l[1],"chemistry":l[2]}
    for key,value in marks.items():
        percent=value//10
        if(percent==10 or percent==9  ):
            print(key,"A+")
        elif(percent==8 ):
            print(key,"A")
        elif(percent==7 ):
            print(key,"B+")
        elif(percent==6 ):
            print(key,"B")
        elif(percent==5 ):
            print(key,"C+")
        elif(percent==4 ):
            print(key,"D+")
        else:
            print(key,"Fail")
            fail=1
    if(fail==1):
        print("Overall FAIL")
    else:
        print("Overall:PASS")
    
else:
    print("invalid set of input")



#better code
"""
#accept percentage of marks from user and display the grade
l=list(map(int,input("enter perfentage of subject physics  maths chemistry respectivly seperated by space").split()))
#to append average percentage(also total percentage)

l.append((l[0]+l[1]+l[2])/3)
fail=0
if(len(l)==4):
    marks={"physics":l[0],"Maths":l[1],"chemistry":l[2],"Total":round(l[3],2)}
    for key,value in marks.items():
        percent=value//10
        if(percent==10 or percent==9 and (key!="Total" or fail==0) ):
            print(key,"A+")
        elif(percent==8 and (key!="Total" or fail==0)):
            print(key,"A")
        elif(percent==7 and (key!="Total" or fail==0)):
            print(key,"B+")
        elif(percent==6 and (key!="Total" or fail==0)):
            print(key,"B")
        elif(percent==5 and (key!="Total" or fail==0)):
            print(key,"C+")
        elif(percent==4 and (key!="Total" or fail==0)):
            print(key,"D+")
        else:
            print(key,"Fail")
            fail=1
"""


