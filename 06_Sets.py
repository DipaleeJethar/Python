# Sets
# Unordered and Unique values
# Duplicate values not allow
my_set = {'mon', 'tue', 'wed'}
print(my_set)

#Adding a new value
my_set.add('fri')
print(my_set)

# To print only unique values
my_list = ['mon', 'tue', 'wed', 'mon', 'tue']
days_set = set(my_list)
print(days_set)