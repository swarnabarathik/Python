string=input("enter the string")
count=0
for i in string:
    if(i.isupper()):
        count+=1
print("Count of ushpper case letters:%d"%count)
