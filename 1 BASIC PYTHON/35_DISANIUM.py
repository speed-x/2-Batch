n = int(input("ENTER A NUMBER : "))
a = n
digits = 0
while(n):
    n = n//10
    digits = digits + 1 
n = a 
sum = 0
while(n):
    b = n%10
    sum = sum + (b**digits)
    digits = digits - 1
    n = n//10
if sum == a:
    print("DIASIUM")
else:
    print("NOT DIASIUM")