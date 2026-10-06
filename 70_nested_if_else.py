# Write a program to find smallest number among has given four numbers without using logical &&(and) operator.
a=int(input("Enter value of a = "))
b=int(input("Enter value of b = "))
c=int(input("Enter value of c = "))
d=int(input("Enter value of d = "))
if a<b:
    if a<c:
        if a<d:
            print(a,"is smallest number")
        else:
            print(d,"is smallest number")
    else:
        if c<d:
            print(c,"is smallest number")
        else:
            print(d,"is smallest number")
else:
    if b<c:
        if b<d:
            print(b,"is smallest number")
        else:
            print(d,"id smallest number")
    else:
        if c<d:
            print(c,"is smallest number")
        else:
            print(d,"is smallest number")