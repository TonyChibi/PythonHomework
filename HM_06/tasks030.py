def arifmeticProgressFiller():
    first =int(input("insert first element of ariphmetic progressive array: "))
    step = int(input("insert the quntity for a step of progression: "))
    ammount=int(input("insert the ammount of elements in array: "))
    progressiveArray=[first]
    for i in range(ammount):
        if i!=0:
            progressiveArray.append(progressiveArray[i-1]+step)
        print(i)
    return progressiveArray
arr=arifmeticProgressFiller()
print(arr)