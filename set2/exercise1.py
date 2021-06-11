"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think it's going to create a list containing: what, does, this, line, do , ?. Which then can be called upon with some_words
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #Stored the words as a list in some_words

#I think it will print every word in the list some_words on each line
for word in some_words:
    print(word) #For every word in the list it was printed on a new line

#I think it works the same as the one above but x is used instead of word so it will print every word on a new line
for x in some_words:
    print(x) #Every word is printed on a new line

#I think this will just print the list within [] brackets on 1 line
print(some_words) #printed the list within [] brackets with each word in '' and with a comma between each item

#I think this will print the string 'some_words contains more than 3 words' if length of the list some_words is larger then 3
if len(some_words) > 3:
    print('some_words contains more than 3 words') #The string 'some_words contains more than 3 words' was printed because within the string there are 6 items so that is larger than 3

#I think this defined the variable usefulFunction as a function that prints the 6 attributes: system, node, release, version, machine, and processor, of the interface.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction() #The function was called so it printed: uname_result(system='Windows', node='LAPTOP-2953OTEI', release='10', version='10.0.19041', machine='AMD64', processor='AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD') which is the attributes of the interface
