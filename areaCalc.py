from math import pi
from os import system

def areaMenu():
    menu=True
    while menu == True:
        system('clear')
        print("""
        Choose shape to calculate area: 
        1. Circle
        2. Triangle
        3. Rectangle
        4. Trapezoid
        5. Exit
        """)
                
        selection=raw_input("Please select: ")

        if selection == '1':
            circleArea()
        elif selection == '2':
            triArea()
        elif selection == '3':
            rectArea()
        elif selection == '4':
            trapArea()
        elif selection == '5':
            menu = None
            
def circleArea():
    system('clear')
    radius = int(raw_input("Enter radius of circle: "))
    print "\nArea of Circle: ", (radius * radius) * pi
    pause = raw_input("\nPress Enter to continue...")
            
def triArea():
    system('clear')
    height = int(raw_input("Enter height of triangle: "))
    base = int(raw_input("Enter length of triangle's base: "))
    print "\nArea of Triangle: ", (height * base) / 2
    pause = raw_input("\nPress Enter to continue...")
    
def rectArea():
    system('clear')
    height = int(raw_input("Enter height of rectangle: "))
    base = int(raw_input("Enter length of rectangle's base: "))
    print "\nArea of Rectangle: ", (height * base)
    pause = raw_input("\nPress Enter to continue...")
    
def trapArea():
    system('clear')
    baseA = int(raw_input("Enter length of top base: "))
    baseB = int(raw_input("Enter length of bottom base: "))
    height = int(raw_input("Enter height of trapezoid: "))
    print "\nArea of Trapezoid: ", ((baseA + baseB) / 2) * height
    pause = raw_input("\nPress Enter to continue...")
        
areaMenu()