n = int(input("ENTER A NUMBER : "))
sum = 0 
for i in range(1,n+1,1):
    if n%i == 0:
        sum = sum + i
print(sum)