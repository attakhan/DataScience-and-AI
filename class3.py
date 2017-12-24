''' A closer look to looping
- print() method contain end parameter whose bydefault value is "\n"
- range(1,5) will generate a numerical list from 1 to 4 .  type of range is <class  'range'>
- list(range(1,5)) will make the numerical list
- ** will used as power of a value
- min , max , sum method will do min , max and sum of all elemnt of list.


'''

'''
example 1
'''
magicians = ["alice", "tom","carolina"]

for magician in magicians:
    print(magician.title() + ", It was a great trick")

print("Thank you All")

'''
example 2
'''
rangeA = range(11,2, -2)
print(list(rangeA))

for item in rangeA:
    print(item)
'''
example 3
'''
squares = []
for value in range(1,11):
    square = value **2
    squares.append(square)

print(squares)

print("This dinner is not that bad!");

s = "This dinner is not that bad!"

