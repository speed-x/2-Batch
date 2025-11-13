n = int(input("ENTER A NUMBER : "))
a = n
rev = 0
while(n):
    b = n%10
    rev = rev*10 + b 
    n = n//10
print(a + rev)