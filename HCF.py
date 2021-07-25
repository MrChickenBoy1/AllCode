num1 = Div = int(input("What is your first number (Divisor)"))
num2 = Divd = int(input("What is your second number (Divident)"))
HCF = 0
rem = 1
OldNum = []


while rem != 0:
    rem = Divd % Div
    if rem != 0:
        Divd = Div
        Div = rem
    
print ("The HCF of", num1, "and", num2, "is", Div)
print (num1/Div, "x", Div, "=", num1 )
print (num2/Div, "x", Div, "=", num2)


