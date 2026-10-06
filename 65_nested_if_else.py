# Check whether a character is vowel, consonant or not an alphabet.
ch=input("Enter a character : ")
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    if ch in "aeiouAEIOU":
        print("alphabet is vowel")
    else:
        print("alphabet is consonant")
else:
    print("character is not alphabet")