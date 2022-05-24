import random

# 3) Отсортировать лист по убыванию
myList = []
for i in range(0, random.randint(5, 20)):
    myList.append(random.randint(-100, 100))
    myList.sort
print(myList)
# Some changes

# 7) Добавить в конец листа элементы 5, 55
myList = []
for i in range(0, random.randint(5, 20)):
    myList.append(random.randint(-100, 100))
myList.extend([5, 55])
print(myList)

# 8) Вывести на экран, первые 3 элемента листа
myList = []
for i in range(0, random.randint(5, 20)):
    myList.append(random.randint(-100, 100))
print(myList[0:3])

# 9) Удалить последний элемент листа, если его длина нечетная
myList = []
for i in range(0, random.randint(5, 20)):
    myList.append(random.randint(-100, 100))
t=int(len(str(myList[-1])))
if t % 2 !=0:
    myList.pop()
print(myList)

# 10) Вывести элемент, который находится по середине листа (Если такого нету, то 0)
myList = []
for i in range(0, random.randint(5, 20)):
    myList.append(random.randint(-100, 100))
x = int(len(myList))
if x %2==1:
    x = x//2
    print(myList[x])
else:
    print("0")