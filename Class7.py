def greet_user():
    print('Hello world')


def greet_user(username):
    print('Hello world',username)


def describe_pet ( petname,animal_tpye = "dog" ):
    print("My animal type is: ",animal_tpye)
    print("my",animal_tpye,"name is ",petname)


def mynames(first,last,middle=''):
    print("Fullname is :",first,middle,last)


def make_shirt(message ,size="large"):
    print("the size of the shirt is :" ,size , ",The message printed on shirt is " ,message )

def describe_city(city,country="Pakistan"):
    print(city,"is in",country)

def addition(num1 , num2 ):
    return num1+num2

''' Function Calling portion'''

sum = addition(13,15)
print(sum)
'''
describe_city("Karachi")
describe_city("Lahore")
describe_city("Sydney","Australia")



make_shirt(16,"Denizen")
make_shirt(size=16,message="Denizen")

make_shirt("I love Phyton")
make_shirt("I love Phyton","medium")
make_shirt("do study R programming","small")




greet_user("Atta")
describe_pet("hamster","harry")

describe_pet(animal_tpye="Hamster" , petname="Harry")
describe_pet(  petname="Harry" , animal_tpye="Hamster")
describe_pet(petname="harry")
mynames("atta","khan")

'''