n = eval(input("ENTER THE MARKS : "))
if n >= 91 and n <= 100:
    print("A")
elif n >= 71 and n < 91:
    print("B")
elif n >= 61 and n <= 70:
    print("C")
elif n >= 33 and n <= 60:
    print("D")
elif n >= 0 and n < 33:
    print("FAIL")
else:
    print("INVALID !!!!!!")