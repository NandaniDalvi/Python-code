print("<===WELCOME TO CONVERTER===>")
print("Press 1 To find area of circle")
print("Press 2 To find area of rectangle")
print("Press 3 To find area of triangle")
print("Press 4 To find area of square")
num=int(input("Enter number = "))
match num:
   case 1:
      print("<<finding area of circle>>")
      radius=float(input("Enter radius = "))
      area=3.14*radius*radius
      print("area of circle = ",area)
   case 2:
      print("<<finding area of rectangle>>")
      lenght=float(input("Enter lenght = "))
      breadth=float(input("Enter breadth  = "))
      area=length*breadth
      print("area of rectangle = ",area) 
   case 3:
      print("<<finding area of triangle>>") 
      base=float(input("Enter base = "))
      height=float(input("Enter height = "))
      area=1/2*base*height
      print("area of triangle",area)
   case 4:
      print("<<finding area of square>>")
      side=float(input("Enter side = "))
      area=side*side
      print("area of square",area)
   case _:
      print("Invail choice")
