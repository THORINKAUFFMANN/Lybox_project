#Exemple
number1 = 471
number2 = 480

#fonction
def calculate(nb):
    res = nb
    i = 10

    while((nb / i) >= 10):
        i = i * 10
    while (i != 1):
        res = res + ((nb / i) % 10)
        i = i / 10
    return res

def manage(nb1, nb2):
    joinpt = 0

    while(nb1 != nb2):
        nb1 = calculate(nb1)
        nb2 = calculate(nb2)
    joinpt = calculate(nb1)
    return joinpt

#main

if(0 < number1 & number1< 20000000 & 0 < number2 & number2 < 20000000) :
    if(manage(number2, number1) > 0 & manage(number1, number2) < 20000000):
        joinpt = manage(number1, number2)
        print(joinpt)
    else :
        print("the rule was not respected2")
else :
    print("the rule was not respected")