print("        <<<----Result Sheet---->>>")
rollno=int(input("Enter your rollNo. = "))
match rollno:
  case 1325:
     print("Name: Mansi Patidar")
     print("Course: DCA")
     print("percentage: 65%")
     print("Pass, Can do better")
  case 4567:
     print("Name: Sujay Khandekar ")
     print("Course: BBA")
     print("percentage: 90%")
     print("Pass, Keep it up")
  case _:
     print("Entered rollNo. is incorrect")