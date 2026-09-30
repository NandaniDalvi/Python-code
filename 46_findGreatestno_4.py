a=int(input("Enter a num1 ="))
b=int(input("Enter a num2 ="))
c=int(input("Enter a num3 ="))
d=int(input("Enter a num4 ="))
if a>b and a>c and a>d:
    print(a,"is greatest number")
elif b>c and b>d:
    print(b,"is greatest number")
elif c>d:
    print(c,"is greatest number")
else:
    print(d,"is greatest number")
