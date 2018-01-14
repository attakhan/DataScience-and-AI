

'''
prompt = "tell me something"
prompt += '\n write quite! to exit the program'
'''
'''
message = ""
while message != 'quit!':
    message = input(prompt)
    if message != 'quit!':
        print(message)

'''


'''
use flag in while loop

active = True
while active:
    message = input(prompt)

    if message == 'quit!':
        active = False
    else:
        print(message)

'''

'''
use break to exit while loop
while True:
    city = input(prompt)

    if city == 'quit!':
        break
    else:
        print("I would love this " + city.title())
'''

'''
use continue to skip code in while loop 
number = 0
while number <= 10:
    number += 1
    if number % 2 == 0:
        continue

    print(number)


for i in range(0,20):

    if i == 15:
        continue

    else:
        print(i)
'''

'''
prompt = 'please provide the list of topping'
prompt += '\n write quit to end'
topping = ''

while topping != 'quit':
    topping = input(prompt)

    if topping != "quit":
        print("i will add all these topping" + topping.title())

    else:
        print("thanks for purchasing pizza")
'''
'''
prompt = 'please provide your age'
prompt += '\n write quit to end'
age = ''

while age != 'quit' :
    age = input(prompt)

    if age == 'quit':
        print("thank you for purchasing tickets")
        break
    elif int(age) < 3:
        print("ticket is free")
    elif int(age) > 12 :
        print("movie ticket cost $15")
    else:
        print("movie ticket cost $10")

'''

'''
unconfirmed_user = ['alice', 'bob' , 'adam']
confirmed_user = []

while unconfirmed_user:
    user = unconfirmed_user.pop()
    print("verifying user" + user.title())
    confirmed_user.append(user)

for cuser in confirmed_user:
    print(cuser.title())

'''
'''
pets = ['dog','cat','lion','cat','sheep','deer','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print(pets)
'''


