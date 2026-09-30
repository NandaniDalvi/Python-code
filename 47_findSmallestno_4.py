a=int(input("Enter a num1 ="))
b=int(input("Enter a num2 ="))
c=int(input("Enter a num3 ="))
d=int(input("Enter a num4 ="))
if a<b and a<c and a<d:
    print(a,"is Smallest number")
elif b<c and b<d:
    print(b,"is Smallest number")
elif c<d:
    print(c,"is Smallest number")
else:
    print(d,"is Smallest number")
