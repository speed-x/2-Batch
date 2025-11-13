n = int(input("ENTER A NUMBER : "))
a = n
digits = 0
while(n):
    digits = digits + 1 
    n = n//10
print(digits)