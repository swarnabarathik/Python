punctuation= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string="Hello!!!, he said ---and went."
no_punc=""
for i in string:
    if i not in punctuation:
        no_punc=no_punc+i
print(no_punc)
        
