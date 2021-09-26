fibo = []

num = int(input ("What is the number till which you need finonacci? "))
while num < 1:
    num = int(input ("What is the number till which you need finonacci? "))

meth = int(input("Which method (1 for fast,2 for slow)?"))

def fib (number):
    if number == 0:
        return 0
        
    if number == 1:
        return 1
    
    if not (meth==1 and fibo[number - 1] and fibo[number - 2]):
        return fib(number - 1) + fib(number - 2)
    else:
        return fibo[number - 1] + fibo[number - 2]

if meth==1:
    for i in range (num):
        fibo.append(fib(i))
else:
    for i in range (num):
        print(fib(i), end=',')

if meth==1:
    #print(fibo)
    for i in range (num):
        print(fibo[i], end=',' )

