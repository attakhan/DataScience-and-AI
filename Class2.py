# lecture 18 november 2017 python crash course chaper 2 and 3  introduction to List
'''
- id() will show memory location of the string
-   array is static and homogenous while list is dynamic and can contain different type of elements.
-   array size is fixed and defined  while list size is not fixed and can contain as many elements.
-
'''

# for example
mylist = []  # the length of the list is zero
mylist2 = [1,2,3,4,5,6]  # size of the list is 6 while the first element is at location 0 so the index is from 0 - 5

print(mylist2)  # whenever we print list it will not print the element of list it will print the complete list

# to access the element of the list we can access through the indexes
print(mylist2[4])

print(mylist2[-1])  # will start the index in reverse order.

print(mylist2[1:3])  # will pick the element in sequence from index 1 to 3 . slice will be happen on index not on length of the list

print (mylist2[-7:-1])  # -1 will indicate the last letter of the list.

print(mylist2[-3:4])

mystirng = ["p","r","0","g","r","a","m","i","z"]

print(mystirng[-3:9])

# title method will convert the first letter of a word as capital
mystringlist = ["ab", "ac"]
print(mystringlist[1].title())


# ----------  Adding , changing and removing of elements --------------------------

''' 
append() append value on the last index
insert() will take 2 input parameters (index , value)
range in -ve will start from last toward the start.
del statement will remove the element from the define index
pop() method will also delete/out the last element or element of specific index of the the list
remove() method will remove the element by the value 
'''


mystringlist.append("ad")

mystringlist.insert(2,"ae")

del mystringlist[0]
mystringlist_popped = mystringlist.pop(1)
mystringlist.remove("ad")


print(mystringlist)
print(mystringlist_popped)


#------------------------------ loopings ---------------------------

for num in range(1,10):
    print(num)


# Task Class work :  remove the element of the list by for loop








