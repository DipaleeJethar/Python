# Conditional statement
if 10<8:
    print("It is True")
else:
    print("It is False")
#---------------------------------------***--------------------------------------
#Another Example
print('Enter a no. to check if that is EVEN or ODD')

num = int(input('Enter a no - '))
if num % 2 == 0:
    print("Yes no is EVEN")
else:
    print("No. is ODD")
#----------------------------------------***--------------------------------------
#Another Example
users = ['Dipalee', 'Priti']
if 'Dipalee' in users:
    print('User Exist')
else:
    print('User does not Exit')
#--------------------------------------***--------------------------------------
#Another Example
marks = int(input('Enter total marks: '))

if marks >= 80:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
else:
    print("Failed!!!!!!")
#-----------------------------------------***-------------------------------------
#If-else Nesting
age = 20
if age >= 18:
    print("You can vote")
else:
    print("Yo cannot vote")
#--------------------------------------------***----------------------------------
#Conditional Statements
#condition1 and condition2
age = 20
voter_id = True
if age >=18 and voter_id:
    print('You can Vote')
else:
    print('You cannot vote!')

#condition1 or condition2
age = 20
voter_id = False
#condition1 and condition2
if age >=18 or voter_id:
    print('You can Vote')
else:
    print('You cannot vote!')