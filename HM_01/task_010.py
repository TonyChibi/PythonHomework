# tokens task


from random import randint
#this one is using a list, i supposed
#makng a pile of tokens
tokens={}
ammount=randint(100,10000)
for i in range(ammount):
    tokens[i]=randint(0,1)

#counting
zeroes=0
for i in tokens:
    if tokens[i]==0:
        zeroes+=1
print(ammount)
print(zeroes)
if ammount-zeroes>zeroes:
    print(f"the less numbers of tokens you need to turn to same side in a pile of {ammount} tokens is {zeroes}")
else:
    print(f"the less numbers of tokens you need to turn to same side in a pile of {ammount} tokens is {ammount-zeroes}")


#experiment
#this one is using an array
tokens=[]
ammount=randint(100,10000)
for i in range(ammount):
    tokens+=[randint(0,1)]

#counting
zeroes=0
for i in tokens:
    if i==0:
        zeroes+=1
print(ammount)
print(zeroes)
if ammount-zeroes>zeroes:
    print(f"the less numbers of tokens you need to turn to same side in a pile of {ammount} tokens is {zeroes}")
else:
    print(f"the less numbers of tokens you need to turn to same side in a pile of {ammount} tokens is {ammount-zeroes}")
