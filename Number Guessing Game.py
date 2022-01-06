import random
import math
print("NUMBER GUESSING GAME")
print("you are allotted 600 points and with each wrong guess 100 points will be deducted from your score")
print("1.Play")
print("2.Exit")
ch=input("enter your choice")
if ch=='1':
    x = random.randint(1, 50)
    chances=5
    points=100
    while chances!=0:
        score=600-points
        chances-=1
        guess = int(input("Guess a number(1-50):- "))
        print( "you have" ,chances, "chances left to guess")
        points+=100   
        if x == guess:
            print("Congratulations you did it ")
            print("your score" , score)
            break
        elif x < guess:
            print("You Guessed too high!")
        elif x > guess:
            print("You guessed too small!")
    print("\nThe number is %d" % x)
elif ch=='2' :
    print("closed")
    exit()



 
