a=int(input("Enter a num1 ="))
b=int(input("Enter a num2 ="))
c=int(input("Enter a num3 ="))
if a<b and a<c:
    print(a,"is a smallest number")
elif b<c:
    print(b,"is a smallest number")
else:
    print(c,"is a smallest number")