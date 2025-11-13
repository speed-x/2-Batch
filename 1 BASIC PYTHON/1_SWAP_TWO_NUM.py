a = eval(input()) # eval automatically detects the data type of the input
b = eval(input()) # used when we dont know what user is about to give in input
c = a
a = b
b = c
print(a,b)
