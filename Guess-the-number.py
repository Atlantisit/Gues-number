#Game "Guess the number"
#Choose a number in the runge 1-100
#The player can guess the number in 10 attemps
#
import random
number = random.randint(1,100)
print ('\nHi! Wellcome to "Guess the number" games.\nYou have only 10 quess.\nYou must input number in the range 1-100.')
quess = ''
tries = 10
while tries > 0:
    tries -=1
    while True:
        print ("You have ",tries," tries")
        quess = input("Choose a number: ")
        if quess.isdecimal():
            quess = int (quess)
            if quess >0 and quess <=100:
                print ("Ok, you number:",quess)
                break
    if quess > number:
        print ("No, the correct number is less")
        continue
    elif quess < number:
        print ("No, the correct number is greater")
        continue
    elif quess == number:
        print ("Wow! You right!")
        break
    #Выводить сколько осталось попыток - done
    #Прелагать сыграть ещё раз
    #Сделай действия функцией, а на верхнем уровне чтобы оно вызввадр функцию сначала,
    #  а потом входило в while True и при ответе да вызывало опять функцию, а при нет выходило