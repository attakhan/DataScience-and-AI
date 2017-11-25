print("Assignment1 Tasks")
# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'

def donuts(count):
    if count < 10:
        result = "Number of Count:" + str(count)
    else:
        result = "Number of Count:" + "many"
    return result


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.

def both_ends(inputstring):
    lenstring = len(inputstring)
    if lenstring > 2:
        string_start = inputstring[:2]
        string_end = inputstring[-2:]
        result = string_start + string_end
    else:
        result = ""
    return result


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    first_letter = s[0]
    for i in range(0,len(s)):
        if i > 0:
            if s[i] == s[0]:
                changed_string=s.replace(s[i],"*")

                print(i)
        else:
            continue
    s = first_letter + changed_string[1:]
    return s


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
    # +++your code here+++

    result = b[:2] + a[2:] + ' ' + a[:2] + b[2:]
    return result
