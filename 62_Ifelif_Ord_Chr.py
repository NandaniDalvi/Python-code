ch=input("Enter character = ")
if ch>='a' and ch<='z':
    ch=chr(ord(ch)-32)
    print("Upper-case: ",ch)
elif ch>='A' and ch<='Z':
    ch=chr(ord(ch)+32)
    print("Lower-case: ",ch)
else:
    print("Please enter an alphabet")