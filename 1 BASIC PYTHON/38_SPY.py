n = int(input("ENTER A NUMBER : "))
a = n
sum = 0
while(n):
    b = n%10
    sum = sum + b
    n = n//10
n = a
prod = 1
while(n):
    b = n%10
    prod = prod * b
    n = n//10
if sum == prod:
    print("SPY NUMBER")
else:
    print("NOT A SPY NUMBER")