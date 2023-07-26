#two integers magic trick

sum=int(input("imagine two integers \n insert the SUM of two integers: "))
mult=int(input("now insert the product of their multiplication: "))


a=sum//2
b=sum-a
breakerCount=0
top=sum
bottom=a
while(a*b!=mult):
    if breakerCount==100:
        break
    print("MAGIC")
    if a*b>mult:
        prev=a
        a=a-(top-bottom)//2
        top=prev
        
    else:
        prev=a
        a=a+(top-bottom)//2
        bottom=prev
    b=sum-a
    breakerCount+=1
    
if breakerCount==100:
    print("are you shure you count them well?")
else:
    print(f"is your integers is {int(a)} and {int(b)}?")
print(breakerCount)