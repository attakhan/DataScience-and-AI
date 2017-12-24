'''
age = 50

if age> 45:
    print("you are a senior citizen. you can vote without standing in queue . ")

elif age >= 18 :
    print("you are old enough to vote")
    print("Have you register for the vote")

else:
    print("you are too young for voting")
    '''
'''
alien_color = []
color = input("enter color")

if alien_color:
    if color in alien_color:
        if color == "green":
            print("the player just earned 5 points")
        else:
            print("the player just earned 0 points")
    else:
        print("the player just earned 0 points")
else:
    print("the list is empty")

'''
selected_friends=[]
my_friends = ["Ahsan" ,"Shahroz","Naeem","Muneeb","Talha","Taha","Salman","Zaheer","Omer","Bilal"]
start_letter = ['A','B','C','D','E','F','G']
'''
for friend in my_friends:
    if friend[0]  in start_letter:
        selected_friends.append(friend)
'''

filterlist = [x for x in my_friends if x[0].upper() in start_letter]
print(filterlist)


def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2:
            if word[0] == word[-1]:
                count += 1

    # +++your code here+++
    return count

result = match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
print(result)


x= [1,2,3,4,5,6,7,8,9,10]

print(x)

new = [z**2 for z in x if z % 2 == 0]
print(new)