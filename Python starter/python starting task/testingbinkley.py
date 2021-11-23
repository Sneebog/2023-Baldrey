list1 = [34, 56, 34, 26, 80, 64, 102, 300, 35, 6, 87, 88]
count = 1
for index in range(0, len(list1)):
    if (list1[index - count] >= 80) and (list1[index - count] <=100):
        item = list1[index - count]
        list1.remove(item)
        count += 1
print(list1)