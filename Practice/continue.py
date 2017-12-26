var=3
while var>0:
    print("Im in iteration",var)
    var-=1
    if var==2:
        continue
        print("Im still in block")
    print("im still alive")
print("Im out of block")
