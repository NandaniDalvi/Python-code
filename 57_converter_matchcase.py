print("<===WELCOME TO CONVERTER===>")
print("Press 1 for Convert weight kg to gram")
print("Press 2 for Convert distance meter to c.m ")
print("Press 3 for Convert indian currency to dollar")
print("Press 4 for Convert temp. celsius to Fahrenheit")
num=int(input("Enter number = "))
match num:
   case 1:
      print("<<Convert kg to gram>>")
      kg=float(input("Enter weight in Kg = "))
      gran=kg*1000
      print("Weight in gram = ",gram)
   case 2:
      print("<<Convert meter to cm>>")
      meter=float(input("Enter distance in meter = "))
      cm=meter*100
      print("Distance in meter = ",meter) 
   case 3:
      print("<<Convert Indian rupees to dollar>>") 
      rupees=float(input("Enter indian rupees = "))
      dollar=rupees/95.87
      print("Dollar = ",dollar)
   case 4:
      print("<<Convert celsius to fahrenheit>>")
      celsius=float(input("Enter temp. in celsius = "))
      fahrenheit=(celsius*9/5)+32
      print("Fahrenheit = ",fahrenheit)
   case _:
      print("Invail choice")
