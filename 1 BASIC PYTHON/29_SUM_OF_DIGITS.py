n = eval(input("ENTER A NUMBER : "))
sum = 0
while(n):
    b = n%10
    sum = sum + b
    n = n//10
print(sum)
