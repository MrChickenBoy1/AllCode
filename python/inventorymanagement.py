#inventory management

#initialising

operation = ""
inventoryNumber = 0
inventoryItem = ""
inventory = ["vomit", "piss","apple", "red grape", "green apple"]


#input for which operation
operation = input("What operation do you want to do? ['Add', 'Replace', 'Take away'] ")
operation = operation.lower()


while operation != "add" and operation != "replace" and operation != "take away":
    operation = input("What operation do you want to do? ['Add', 'Replace', 'Take away'] ")




#-------if operation is add-------

if (operation == "add"):
    #input for which inventory elemment
    inventoryItem = input("What do you want to add? ")


    #adding that element
    inventory.append(inventoryItem)
    print ("-------------", inventory, "-------------")

#-------if operation is Replace-------

if (operation == "replace"):
    #input for which inventory elemment
    inventoryItem = input("What do you want to replace the item with? ")

    #input for which item element to replace
    print ("-------------", inventory, "-------------")
    inventoryNumber = int(input("There are 5 spaces, which space do you want to replce? "))

    while inventoryNumber >= 5 and inventoryNumber <= 1:
        inventoryNumber = int(input("There are 5 spaces, which space do you want to replce? "))

    #replacing that element
    inventory[inventoryNumber - 1] = inventoryItem
    print ("-------------", inventory, "-------------")

#-------if operation is subtract-------

if (operation == "add"):
    #input for which inventory elemment
    inventoryItem = input("What do you want to add? ")


    #adding that element
    inventory.append(inventoryItem)
    print ("-------------", inventory, "-------------")

