names=["ajai","Amal","sanal","rajesh","ravi","ajmal"]
names=[item.lower() for item in names]
print(names)
count=0
for item in names:
    if(item[0]=='a'):
        count=count+1
print("No of names start with A is ",count)
