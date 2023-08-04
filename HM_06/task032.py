from random import randint

def findIndexesInRange(arr, area, index=0):
    while(index<len(arr)):
        if arr[index]>=area[0] and arr[index]<=area[1]:
            print(f"{index}", end=" ")
        index+=1

arr=[randint(0,1000) for i in range (randint(10,100))]
print(arr)
findIndexesInRange(arr,[100, 500])
