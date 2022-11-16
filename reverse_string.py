# import the abstract stack class

import stack

# create a string
string  = ".tuo tsal ni tsrif ,OLIF ,kcats a htiw gnirts a esrever ot woH"

# create an empty string 
reverse_string = ""

# create a new stack
s = stack.Stack()

# loop over the characterers in the string and push each char to the empty stack
for char in string:
    s.push(char)

# while the stack is not empty add the last character in the stack to the empty string
while s.is_empty() == False:

    reverse_string = reverse_string + str(s.pop())

# print the outcome
print(reverse_string)