string1="I Like C"
string2="Mary Likes Python"
char=""
char1=""
for i in string1:
    if(i.isupper()):
        char+=i
for i in string2:
    if(i.isupper()):
        char1+=i
resultant_string=char+char1
print("Resultant string:",resultant_string)
