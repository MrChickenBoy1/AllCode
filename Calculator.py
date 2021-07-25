#Calculator

#Variable assigning 
Total = 0

def Choosing ():
    while True:
        Mode = int(input('''Addition - 1    Substraction - 2
    Division - 3    Multiplication - 4 '''))
        if 1 <= Mode <= 4:
            break
        else: print ("Invalid input.")
    return Mode

Choosing()

def Print_Message(op):
    global Run_num
    Run_num = int(input(f"How many times should the number be {op}ed? "))


def Add(Run_num, Total):
    for i in range (Run_num):
        Num = int(input(f"What is the number {i+1}: " ))
        Total += Num
    print ("The answer is:", Total)


def Substract(Run_num, Total):
    for e in range (Run_num):
        Num = int(input(f"What is the number {e + 1}:"))
        if e == 0:
            Total = Num
            
        if e != 0:
            Total -= Num
    print ("The answer is:", Total)


def Division (Run_num, Total):
    for f in range (Run_num):
        Num = int(input(f"What is the number {f + 1}:"))
        if f == 0:
            Total = Num

        if f != 0:
            Total  /= Num

    print ("The answer is:", Total)
    

def Multiply (Run_num, Total, numbers):
    Total = 1

    for g in range (Run_num):
        
        Num = int(input(f"What is the number {g + 1}:"))


        Total *= Num
    
        
    print ("The answer is:", Total)
        


if Choosing().Mode == 1:
    Print_Message("add")
    Add(Run_num, Total)

elif Mode == 2:
    Print_Message("subtract")
    Substract(Run_num, Total)

elif Mode == 3:
    Print_Message("divid")
    Division (Run_num, Total)

elif Mode == 4:
    Print_Message("multiply")
    Multiply (Run_num, Total)
