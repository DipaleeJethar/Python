from audioop import reverse
from collections import UserList
#Lists
users_list = ['Dipalee', 'Priti', 'Sayali', 'Mangesh']
print(users_list[0])
print(users_list[3])
print(users_list[-1])

#modify lists
#Adding item to aa list
users_list.append('Manoj')
print(users_list)

#To delete values from a list
users_list.remove('Sayali')
print((users_list))

#To modify values from a list
users_list[2] = 'Priti Jadhao'
print(users_list)

#Adding item to a list at given position
users_list.insert(1, 'Anjali')
print(users_list)

#How to delete values from a list using index no?
del users_list[4]
print(users_list)

#No of items in a list
print(len(users_list))

#Sorting of List Item
users_list.sort()
print(users_list)

#Reverse Sorting
users_list.sort(reverse=True)
print(users_list)
#OR
users_list.reverse()
print(users_list)

#Popping the item in list
UserList = ['Dipalee', 'priti', 'Sayali', 'Sham']
UserList.pop()

print(UserList)

#Slicing lists
#getting first two items
print(UserList[0:2])

#Getting middle 3 items
print(UserList[1:4])

#getting last 2 items
#print(UserList[-2:])

#numeric List
marks = [50, 30, 55, 100, 45, 96]
print(marks)

#print Min marks
print(min(marks))

#print max marks
print(max(marks))

#sum of marks
print(sum(marks))


