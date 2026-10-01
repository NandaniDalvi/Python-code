print("<===WELCOME TO CALCULATOR===>")
print("Press 1 for addition")
print("Press 2 for subtraction")
print("Press 3 for multiplication")
print("Press 4 for division")
num=int(input("Enter number = "))
match num:
   case 1:
     print("<<Performing addition>>")
     a=int(input("Enter 1st number ="))
     b=int(input("Enter 2nd number ="))
     c=a+b
     print(c,"is the addition of given number")
   case 2:
     print("<<Performing subtraction>>")
     a=int(input("Enter 1st number ="))
     b=int(input("Enter 2nd number ="))
     c=a-b
     print(c,"is the subtraction of given number")
   case 3:
     print("<<Performing multiplication>>")
     a=int(input("Enter 1st number ="))
     b=int(input("Enter 2nd number ="))
     c=a*b
     print(c,"is the multiplication of given number") 
   case 4:
     print("<<Performing division>>")
     a=int(input("Enter 1st number ="))
     b=int(input("Enter 2nd number ="))
     c=a/b
     print(c,"is the division of given number")
   case _:
    print("Please press correct number from 1 to 4")
    print("<<<<--THANK UH FOR USING CALCULATOR-->>>>")
