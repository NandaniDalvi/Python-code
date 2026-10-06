# check number is even-positive,even-negative,odd-positive and odd-negative or zero
num=int(input("Enter a number : "))
if num==0:
    print("num is zero")
elif num%2==0:
    if num>0:
        print(num,"even-positive")
    else:
        print(num,"even-negative")
else:
    if num>0:
        print(num,"odd-positive")
    else:
        print(num,"odd-negative")
