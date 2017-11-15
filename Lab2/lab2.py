list1 = [32, 2, 4, 34, 1]

list2 = [list1[0], list1[-1]]

list3 = []

list4 = []

newl1 = [11, 2, 33, 5, 6, 21]
newl2 = [43, 1, 21, 2, 33, 7, 35, 67, 2]

list5 = []

for value in list1:
    if value < 5:
        list3.append(value)
print(list3)

def num(n):
    for value in list1:
        if value < n:
            list4.append(value)
    print(list4)

for one in newl1:
    for two in newl2:
        if one == two:
            list5.append(two)
for five in list5:
    for fivee in list5:
        if five == fivee:
            list5.remove(fivee)
print(list5)


def prime(n):
    flag = False;
    for i in range(n):
        if i!= 0 and i!= 1 and n % i == 0:
            flag = True
       
    if flag:
        print("It's not a prime number")
    else:
        print("It's a prime number")
        
