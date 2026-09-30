ch=input("Enter alphabet =")
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    print(ch,"is alphabet")
elif ch>='0' and ch<='9':
    print(ch,"is Digit character")
else:
    print(ch,"is special character")