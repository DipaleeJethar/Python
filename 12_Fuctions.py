#Functions
#example 1
def greeting():
    print('-' * 20)
    print('Welcome User')
    print('Thank you for signing in...')
    print('-' * 20)
#Calling a function
greeting()
greeting()

#Example 2
def Greetings(user_name):
    print('-' * 20)
    print(f'Welcome {user_name}')
    print('Thank you for signing in...')
    print('-' * 20)
#calling a function
Greetings('Dipalee')
Greetings('Priti')

#Example 3  Dynamic Arguments *
def Interests(user_name, *hobbies):
    print('-' * 20)
    print(f'welcome {user_name}')
    print('Hobbies are: ')
    for hobby in hobbies:
        print(f'- {hobby}')
    print('Thank you for signing in....')
    print('-' * 20)
#Calling a function
Interests('Dipalee', 'Signing', 'Dancing','Playing')
Interests('Priti', 'Signing', 'Playing')

#Exampele 4 Dynamic Arguments **
def interest(user_name, **user_info):
    print('-' * 20)
    print(f'Welcome {user_name}')
    for key, value in user_info.items():
        print(f'{key} is {value}')
    print('Thank you for singing in....')
    print('-' * 20)
#calling a function
interest('Raju', age=18, city='Pune', email='ragj@gmail.com')
interest('Baburao', age=50, city="Maumbai")

#Example 5 Return result in functions
def add(num1 , num2):
    return num1 + num2
result = add(10,20)
print(result)



