List1 = ["von" , 2, 3, 4]
List2 = ["Ay", "Be", "Sea", "De"]
List3 = []

List1_index = 0
List2_index = 0

length = len(List2) * 2

for i in range(0, length):
    x = List1[List1_index]
    e = List2[List2_index]
    List3.append(x)
    List3.append(e)
  

    
    
print(List3)
