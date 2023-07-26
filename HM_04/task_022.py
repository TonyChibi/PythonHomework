from random import randint



n=int(input("insert number for length for a first list: "))
m=int(input("insert number for length for a first list: "))

first_list=[randint(0,10) for i in range(n)]
second_list=[randint(0,10) for i in range(m)]
print(first_list)
print(second_list)
both=set(first_list+second_list)
both=list(both)
both.sort()
print(both)