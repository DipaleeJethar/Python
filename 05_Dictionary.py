#Dictionaries  key:values
marks = {'Hindi': 80, 'English' : 45 }
print(marks)
print(type(marks)) #to check the types
print(marks['English'])

#Another example
car = {'brand': 'Audi', 'model': 'Q3'}
print('Brand of cra is ' + car['brand'])
print('MOdel of car is ' + car['model'])
print(car.get('price')) #output is empty that is none

#Adding item to a dictionary
car['price'] = 1000000
print(car)

#to delete values from a dictionary
del car['model']
print(car)

#Getting no. of key values in dictionary
print(len(car))
