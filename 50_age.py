age=int(input("Enter age = "))
if age>=0 and age<=12:
    print("your age is",age,"then ur child")
elif age>=13 and age<=18:
    print("your age is",age,"then ur teenager")
elif age>=19 and age<=50:
    print("your age is",age,"then ur adult")
elif age>50 and age<=100:
    print("your age is",age,"then ur senior citizen")
else:
    print("Please enter valid age")