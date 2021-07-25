List2 = []
List1 = ["a", "b", "c", "e", "f"]

x = 0
i = len(List1)

for e in range (0, i, 2):
    print (e)
    x = List1[e]
    List2.append(x)
    

    
print(List2)
  
