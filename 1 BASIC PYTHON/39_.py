n = int(input("ENTER A NUMBER : "))
a = n
sum = 0
prod = 1
while(n):
    b = n%10
    sum = sum + b
    prod = prod * b
    n = n//10
n = a
if sum == prod:
    print("SPY NUMBER")
else:
    print("NOT A SPY NUMBER")