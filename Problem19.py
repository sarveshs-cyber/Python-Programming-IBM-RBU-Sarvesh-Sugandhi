a = int(input("Enter First Number:"))
b = int(input("Enter Second Number"))
c = input("What to do?")

if 'sum' in c:
    print("sum is " ,a+b)
elif 'subtract' in c:
    print("Subtarction is ", a-b)
elif 'multiply' in c:
    print("Multiplication is", a*b)
elif ' division' in c:
    print("Division is ", a/b)
else:
    print("Invalid Entery!")                