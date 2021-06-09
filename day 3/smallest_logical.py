n1=int(input("Enter the number1: "))
n2=int(input("Enter the number2: "))
n3=int(input("Enter the number3: "))
if n1>n2 and n3>n2:
    print(n2,"is the smallest number")
elif n2>n1 and n3>n1:
    print(n1,"is the smallest number")
else:
    print(n3,"is the smallest number")

