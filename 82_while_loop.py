#WAP to display sum 1 to n(given number)
n=int(input("Enter a number till u want to display = "))
i=1
res=0
while i<=n:
    res=res+i
    i+=1 
print(f"sum of 1 to {n} = {res}")
