#Age guesser

Input = input ("Pick a number from 1 - 9: ")


num = int(Input)

if num > 9:
    print("No, pick again by running the program again.")

else:
    print ("Number Stored")

print("Now the number will be multiplied by two: ")

Multi = num * 2
print (Multi)

print ("5 will be added to the number: ")

Minus = Multi + 5

print (Minus)

print("The number will be multiplied by 50 now: ")

Multiplied = Minus * 50

print (Multiplied)




Input_2 = input ("If your birthday happened in 2021, add 1771, else add 1770. Only add these two numbers")

num_2 = int (Input_2)

if num_2 == 1770:
    new_num = Multiplied + 1770
elif num_2 == 1771:
    new_num = Multiplied + 1771

Final = input ("Now just take away you year of birth from this number")

FINAL = int(Final)

print (new_num - FINAL)






