operation = input("Create a file or Read a file? ")


if  operation == "file.create":
    file_name = input ("What file name do you want? ")
    with open(file_name, "w") as file:
        text = input("Write you text: ")
        file.write(text)
elif operation == "file.read":
    file_name = input("What file? (case sensitive) ")

    try:
        with open(file_name, "r"    ) as file:
            text = file.readline()
            print (text)
    except:
        print ("file not found (Check if you've written the name right)")