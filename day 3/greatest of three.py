n1=int(input("Enter the number1: "))
n2=int(input("Enter the number2: "))
n3=int(input("Enter the number3: "))
if n1>n2:
    if n1>n3:
        print(n1,"is the greatest number")
    else:
        print(n3,"is the greatest number")
elif n2>n3:
    if n2>n1:
        print(n2,"is the greatest number")
    else:
        print(n1,"is the greatest number")
else:
    print(n3,"is the greatest number")


