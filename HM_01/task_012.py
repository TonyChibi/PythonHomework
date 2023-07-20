#two integers magic trick

sum=int(input("imagine two integers \n insert the SUM of two integers: "))
mult=int(input("now insert the product of their multiplication: "))


a=sum/2
b=sum-a
breakerCount=0
while(a*b!=mult):
    if breakerCount==100:
        break
    print("MAGIC")
    prev=int(a)
    if a*b>mult:
        a=a-prev/2
    else:
        a=a+prev/2
    b=sum-a
    breakerCount+=1
if breakerCount==100:
    print("are you shure you count them well?")
else:
    print(f"is your integers is {int(a)} and {int(b)}?")