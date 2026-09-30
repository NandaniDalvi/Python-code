num=int(input("Enter a num  for month = "))
if num==2:
    print("28 Days")
elif num in (1,3,5,7,8,10,12):
    print("31 Days")
elif num in(4,11,6,9):
    print("30 Days")
else:
    print("Enter a number according to month")