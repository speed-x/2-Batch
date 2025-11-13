n = int(input("ENTER A NUMBER : "))
prod = 1
while(n):
    b = n%10
    prod = prod * b
    n = n //10
print(prod)