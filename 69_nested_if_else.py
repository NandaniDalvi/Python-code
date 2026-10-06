# Write a program to find greatest number among has given four numbers without using logical &&(and) operator.
a=int(input("Enter value of a = "))
b=int(input("Enter value of b = "))
c=int(input("Enter value of c = "))
d=int(input("Enter value of d = "))
if a>b:
    if a>c:
        if a>d:
            print(a,"is greatest number")
        else:
            print(d,"is greatest number")
    else:
        if c>d:
            print(c,"is greatest number")
        else:
            print(d,"is greatest number")
else:
    if b>c:
        if b>d:
            print(b,"is greatest number")
        else:
            print(d,"id greatest number")
    else:
        if c>d:
            print(c,"is greatest number")
        else:
            print(d,"is greatest number")