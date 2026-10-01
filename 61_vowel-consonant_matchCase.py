alpha=input("Enter alphabet = ")
match alpha:
   case "a"|"e"|"i"|"o"|"u":
     print("Vowel")
   case _:
    print("Consonant")