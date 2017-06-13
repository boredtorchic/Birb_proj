# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""


User_input1 = raw_input("Type in a word and il see if its a pannagram: ")
print User_input1 [::-1]
if User_input1 == User_input1 [::-1]:
    print "It is"
else: print "no its not"


    #int(len(User_input1)) -= 1
#while len(word: word[0]==word[-1] word[1:-1}