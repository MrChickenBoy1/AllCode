List1 = [1, 2, 3]
List2 = ["A", "B", "B"]

x = 0
Len = len(List2)
for i in range(0, Len):
    print ()
    ele = List2[x]
    List1.append(ele)
    x += 1

print (List1)
