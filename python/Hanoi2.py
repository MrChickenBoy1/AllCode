import pygame

WIN = pygame.display.set_mode((500, 500))

def wait():
    #input("Press enter to continue...")
    pass

def hanoi(n,frmT,auxT,toT,maxdisk):
    global turns
    if n==0:
        return
    hanoi(n-1,frmT,toT,auxT,maxdisk)
    toT[0].append(frmT[0].pop())
    print( "Moving disk", n ,"from tower", frmT[1],"to tower",toT[1])
    print(frm[0],aux[0],to[0])
    #movedisk(n,frm[0],aux[0],to[0],maxdisk)
    hanoi(n-1,auxT,frmT,toT,maxdisk)

def movedisk(n,Pfrm,Paux,Pto,maxdisk):
    global turns
    turns+=1
    #print(n,Pfrm,Paux,Pto)
    TmpF,TmpA,TmpT = Pfrm, Paux,Pto
    lenF, lenA, lenT =  len(Pfrm), len(Paux), len(Pto)
    padding = 30
    if(maxdisk<16):
        lineSym = '━━'
    else:
        lineSym = '━'
    print(sep="\n")
    print("Tower A".center(padding) + "Tower B".center(padding) +"Tower C".center(padding))
    print("-------".center(padding) + "-------".center(padding) +"-------".center(padding))
    for i in range (maxdisk,0,-1):

        a,b,c,x="".center(padding),"".center(padding),"".center(padding),""
        if(lenF>=i):
            disk = Pfrm[i-1]
            a = (disk* lineSym).center(padding, " ")
        if(lenA>=i):
            disk = Paux[i-1]
            b = (disk* lineSym).center(padding, " ")
        if(lenT>=i):
            disk = Pto[i-1]
            c = (disk* lineSym).center(padding, " ")
        x = a + b + c           
        print (x)

    print((padding*3*"_").center(padding*3))
    wait()
    
global turns

turns=0

n = 3


frm = [list(range(n,0,-1)),"A"]
to = [[],"C"]
aux = [[],"B"]
#print(frm[0],aux[0],to[0])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #movedisk(n,frm[0],aux[0],to[0],n)
    hanoi(n,frm,aux,to,n)
print ("done in " + str(turns-1) + " turns")
