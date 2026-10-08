#WAP to display odd number series.
i=int(input("Enter staring range  = "))
n=int(input("Enter ending range  = "))
while i<=n:
    if i%2!=0:
        print(i,end="  ")
    i+=1