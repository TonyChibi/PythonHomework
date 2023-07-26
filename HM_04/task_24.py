from random import randint
N=randint(5,10)
bushes=[randint(0,19) for i in range(N)]
print(N)
print(bushes)
max=0
for i in range(N):
    if i+1>=N:
        if bushes[i]+bushes[i-1]+bushes[0]>max:
            max=bushes[i]+bushes[i-1]+bushes[0]
    elif i-1<0:
        if bushes[i]+bushes[N-1]+bushes[i+1]>max:
            max= bushes[i]+bushes[N-1]+bushes[i+1]
    elif bushes[i]+bushes[i+1]+bushes[i-1]>max:
        max=bushes[i]+bushes[i+1]+bushes[i-1]
print(max)