# Write a program to find smallest number among has given three numbers without using logical &&(and) operator.
a=int(input("Enter value of a = "))
b=int(input("Enter value of b = "))
c=int(input("Enter value of c = "))
if a<b:
    if a<c:
        print(a,"is a smallest number")
    else:
        print(c,"is a smallest number")
else:
    if b<c:
        print(b,"is a smallest number")
    else:
        print(c,"is a smallest number")