list1 = [22,22,22,111,12,3,4,4]
list2 = [22,111,23,2,3,4]

common = list(set(list1)) and set(list2)
print(common)
unique = list(set(list1)) or set(list2)
print(unique)