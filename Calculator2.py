#This is going to be way better than before but really small because well eval() is a thing
#This is a test for eval(). It takes a string, and witht the correct syntax it will solve the string for you
# Meaning this is useful for calculators as you don't have to create functions for all opeerations.

print ("------This is a test for eval()-------")
print ("Eval takes a specifc syntax.")
print ("For addition : + | For substraction : - | For multiplication : * | For division: / | Don't write '0' before intergers")

from math import *


print ("")
number = input ("What is input? ")

print ("")
print("Your final answer is: ", eval(number))

eval(number) + 5

