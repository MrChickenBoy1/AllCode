#Arrays test


Class1 = []

Class2 = []

Class3 = []

total = 0

Num = 0

loops = int(input("How many times should the loop be looped? "))

for i in range (loops):
    num1 = int(input(f"What is number {i + 1} for class 1? "))
    Class1.append(num1)
    num2 = int(input(f"What is number {i + 1} for class 2? "))
    Class2.append(num2)
    Class3.append(Class1[i] + Class2[i])

print ("----------Program Info----------")

print ("class one is:", Class1)

print ("class two is:", Class2)


Class1.extend(Class2)

print ("The total of each the digits of the classes is: ", Class3)


for j in range (len(Class1)):
    total = total + Class1[j]

print ("The total of all the digits is:", total)

Class3.sort()
print ("The third list in ascending order is:", Class3)

Class3.sort(reverse = True)

print ("The third list in decending order is:", Class3)
