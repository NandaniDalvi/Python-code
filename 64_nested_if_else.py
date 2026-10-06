# Write a program to read the age of a candidate and determine whether he is eligible to cast his/her own vote in india or not.
country=input("Enter country name : ")
if country=='india':
    age=int(input("Enter your age : "))
    if age>=18:
        print("You are eligible to vote in india")
    else:
        print("You are not eligible to vote in india")
else:
    print("Your not indian")