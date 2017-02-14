from random import randint

randNumber = randint(0,100)

guessNumber = input("Enter a number between 0 and 100: ")

while guessNumber != randNumber:
    if guessNumber > randNumber:
        print "Too high! Guess again: "
        guessNumber = input("Enter a number between 0 and 100: ")
    else:
        print "Too low! Guess again: "
        guessNumber = input("Enter a number between 0 and 100: ")
        
if guessNumber == randNumber:
    print "You got it!"