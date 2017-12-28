string="madam"
string=string.casefold()
rev_string=string[::-1]
if string==rev_string:
    print("Palindrome")
else:
    print("Not palindrome")
