n = int(input("ENTER A YEAR : "))
if n%400 == 0:
    print("LEAP YEAR")
else:
    if n%4 == 0 and n%100 != 0 :
        print("LEAP YEAR")
    else:
        print("NOT LEAP YEAR")