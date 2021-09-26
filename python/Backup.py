import sys
#Box maker thingy

Grid = [[ "_" ] * 3 for i in range (3)]


#Makes the grid
def initialise (Grid):
    for i in range (3):
        for j in range (3):
            print(Grid[i][j], end = '|')
        print ("")


#Askes for input of x, o
def Input (Grid): 
    for i in range (6):
        print (i)
        if i == 5:
            Last (Grid)
            sys.exit()
        
        #Askes for x
        num = input ("X, what row do you want? ")
        
        num1 = input ("X, what col do you want? ")

        #Checks if viable 

        if  Grid[int(num) - 1][int(num1) - 1] !=  "X"  and Grid[int(num) - 1][int(num1) - 1] !=  "O" :
            Grid[int(num) - 1][int(num1) - 1] =  "X" 
        else:
            print ( "No, restart game" )
            Grid = [["_"]*3 for i in range (3)]
            initialise (Grid)
            Input (Grid)
            break
        
        if i == 4:
            Last (Grid)
            sys.exit()
        
        for row in range (3):
            for col in range (3):
                print (Grid[row][col], end = '|')
            print ("")
        
        #Askes for O
        Winning(Grid)
        
        num1_1 = input ("O, what row do you want? ")

        num1_2 = input ("O, what col do you want? ")

        #Checks if viable 
        
        if Grid[int(num1_1) - 1][int(num1_2) - 1] !=  "X"  and Grid[int(num1_1) - 1][int(num1_2) - 1] !=  "O"  :
            Grid[int(num1_1) - 1][int(num1_2) - 1] =  "O" 

        else:
            print ( "No, restart game" )
            Grid = [["_"]*3 for i in range (3)]
            initialise (Grid)
            Input (Grid)
            break
            

        
        for row in range (3):
            for col in range (3):
                print (Grid[row][col], end = '|')
            print ("")
        Winning(Grid)
    
def Winning (Grid):
    #Down
    for e in range (3):
        if Grid[0][0] ==  "X"  and Grid[0][1] ==  "X"  and Grid [0][2] ==  "X" :
            print ("X has won")
            sys.exit()

        elif Grid[0][0] ==  "O"  and Grid[0][1] ==  "O"  and Grid [0][2] ==  "O"  :
            print ("O has won")
            sys.exit()
            
        if Grid[1][0] ==  "X"  and Grid[1][1] ==  "X"  and Grid [1][2] ==  "X" :
            print ("X has won")
            sys.exit()
            
        elif Grid[1][0] ==  "O"  and Grid[1][1] ==  "O"  and Grid [1][2] ==  "O" :
            print ("O has won")
            sys.exit()               

        if Grid[2][0] ==  "X"  and Grid[2][1] ==  "X"  and Grid [2][2] ==  "X" :
            print ("X has won")
            sys.exit()
            
        elif Grid[2][0] ==  "O"  and Grid[2][1] ==  "O"  and Grid [2][2] ==  "O" :
            print ("O has won")
            sys.exit()
        
        #Up

        if Grid[0][0] ==  "X"  and Grid[1][0] ==  "X"  and Grid [2][0] ==  "X" :
            print ("X has won")
            sys.exit()

        elif Grid[0][0] ==  "O"  and Grid[1][0] ==  "O"  and Grid [2][0] ==  "O"  :
            print ("O has won")
            sys.exit()

        if Grid[0][1] ==  "X"  and Grid[1][1] ==  "X"  and Grid [2][1] ==  "X" :
            print ("X has won")
            sys.exit()
            
        elif Grid[0][1] ==  "O"  and Grid[1][1] ==  "O"  and Grid [2][1] ==  "O" :
            print ("O has won")
            sys.exit()

        if Grid[0][2] ==  "X"  and Grid[1][2] ==  "X"  and Grid [2][2] ==  "X" :
            print ("X has won")
            sys.exit()

        elif Grid[0][2] ==  "O"  and Grid[1][2] ==  "O"  and Grid [2][2] ==  "O" :
            print ("O has won")
            sys.exit()

        # Diagonals


        if Grid[0][0] ==  "X"  and Grid[1][1] ==  "X"  and Grid[2][2] ==  "X" :
            print ("X has won")
            sys.exit()

        elif Grid[0][0] ==  "O"  and Grid[1][1] ==  "O"  and Grid[2][2] ==  "O" :
            print "O has won")
            sys.exit()


        if Grid[0][2] ==  "X"  and Grid[1][1] ==  "X"  and Grid[2][0] ==  "X" :
            print ("X has won")
            sys.exit()

        elif Grid[0][2] ==  "O"  and Grid[1][1] ==  "O"  and Grid[2][0] ==  "O" :
            print ("O has won")
            sys.exit()

def Last (Grid):
    print ("Tie, no-one won!")
        
            





            

initialise (Grid)
Input (Grid)


