#!python3
# Volume Calculator
# Feel free to rename your variables
import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print("========================")
    print("========================")
    print("Welcome to the Calculator")
    print("========================")
    print("========================")
    e=input("Press The Enter Key to Begin")

    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print("Choose a Shape: Square, Circle, Triangle, Rectangle")
    a=input(">>> ")
    pass    

def squareArea():
    print("Type any Number for 1")
    t=input(">>>")
    t=int(t)
    t=(t**2)
    print (t)

def circleArea():
    print("Type any Number for 1")
    t=input(">>>")
    t=int(t)
    t=(math.pi * t**2)
    print(t)

def triangleArea():
    print("Type any Number for 1")
    t=input(">>>")
    print("Type any Number for 2")
    f=input(">>>")
    t=int(t)
    f=int(f)
    t=(t*f/2)
    print(t)

def rectangleArea():
    print("Type any Number for 1")
    t=input(">>>")
    print("Type any Number for 2")
    f=input(">>>")
    t=int(t)
    f=int(f)
    t=(t*f)
    print(t)

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    instructions()
    squareArea()
    circleArea()
    triangleArea()
    rectangleArea()


main()