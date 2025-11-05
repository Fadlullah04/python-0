#Let's modify a dictionary
abdurrahman = {
    'Name': 'Abdurrahman', 
    'Age': 21, 
    'Passion': 'Artificial Intelligence',
    }

print(abdurrahman)

#Add values to the dictionary
abdurrahman['Best Car'] = 'Lamborghini'
abdurrahman['Best movie'] = 'Avengers'
print(abdurrahman)

#Let's start with an empty dictionary

life = {}

life['Hurdles'] = 'Real'
life['Success'] = 'Determined'
life['Death'] = True

print(life)

#Now modifying the values
life['Hurdles'] = 'Overcome'
life['Success'] = 'Work for it'

print('The values have now been changed, check them out' + '\n')
print(life)

#Now something more interesting, let's use the dictionary to update my info
#Delete Age
del abdurrahman['Age']
DOB = input('What is your date of birth?')

abdurrahman['Date of Birth'] = DOB
print(abdurrahman['Date of Birth'])

Age = 2025 - int(DOB)

abdurrahman['Age'] = Age
print(abdurrahman)

#Let's loop through a dictionaay
for k, v in abdurrahman.items():
    print("Key: " + k)
    print('Value: ' + str(v) + '\n')
