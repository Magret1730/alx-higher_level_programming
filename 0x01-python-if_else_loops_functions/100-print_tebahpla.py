#!/usr/bin/python3
result = ""    
for i in range(122, 96, -1):
    if i % 2 == 0:
        #print("{}".format(chr(i)), end="")
        result = result + chr(i)
    elif i % 2 != 0:
        #print("{}".format(chr(i - 32)), end="")
        result = result + chr(i - 32)
print(result)
