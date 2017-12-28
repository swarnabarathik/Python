string=" An apple a day keeps the doctor away "
string=string.replace(" ","")
print(string)
resultant_string=string[::2]
print("Resultant string:",resultant_string)
reversed_string=resultant_string[::-1]
print("reversed string:",reversed_string)
