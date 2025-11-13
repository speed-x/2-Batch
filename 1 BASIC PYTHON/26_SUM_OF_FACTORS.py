# SUM OF FACTORS OF A NUMBER 
n = int(input("ENTER A NUMBER : "))
sum = 0
i = 1
while(i <= n):
    if n%i == 0:
        sum = sum + i
    i = i + 1
print(sum)