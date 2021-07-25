List1 = []
List2 = []

Length = int(input ("What is the length? "))


e = Length
e = e + 1

for i in range (0, Length):
    ele = str(input())
    List1.append(ele)

y = len(List1)

 
for e in range(0, Length):        
    y = y - 1
    i = List1[y]
    List2.append(i)



Norm = List1
Reverse = List2


print (Reverse)
if (Norm == Reverse):
    print ("Yes")
   
else:
    print("No")
    
   
