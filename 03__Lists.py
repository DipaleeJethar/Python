from audioop import reverse

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
