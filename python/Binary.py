#num = int(input ("What is your number? "))
msg = input("Enter message ")
#Base = int(input("Enter the base you want for conversion "))

lstmsg = [ord(c) for c in msg]
print (lstmsg)
msgback = [chr(c) for c in lstmsg]
print (msgback)
print (''.join(map(str,msgback)))

def Convertor (number, bs):
    lst = []
    while number / bs != 0:
        lst.append(number % bs)
        number = int(number/bs)
    lst.reverse()
    return lst


#numList = Convertor(num, Base)
#print (numList)
