num=int(input("enter a num = "))  
if num%3==0 and num%5==0 and num%8==0:
    print("num is multiple of 3,5,8")
elif num%3==0 and num%5==0 :
    print("num is multiple of 3,5")    
elif num%3==0 and num%8==0 :
    print("num is multiple of 3,8") 
elif num%8==0 and num%5==0 :
    print("num is multiple of 8,5")   
elif num%3==0:
    print("num is multiple of 3")           
elif num%5==0:
    print("num is multiple of 5")     
elif num%8==0:
    print("num is multiple of 8")     
else:
    print("not multiple of 3,5,8")