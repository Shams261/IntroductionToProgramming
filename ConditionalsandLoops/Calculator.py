#Write a program that performs the tasks of a simple calculator. 
# The program should first take an integer as input and then based on that integer perform the task as given below.

while True:
    i = int(input())
    if(i == 1):
        a = int(input())
        b = int(input())
        c = a+b
        print(c)
    elif(i == 2):
        a = int(input())
        b = int(input())
        c = a-b
        print(c)
    elif(i == 3):
        a = int(input())
        b = int(input())
        c = a*b
        print(c)
    elif(i == 4):
        a = int(input())
        b = int(input())
        c = a/b
        print(int(c))
    elif(i == 5):
        a = int(input())
        b = int(input())
        c = a%b
        print(int(c))
    elif(i == 6):
        exit()
    else:
        print("Invalid Operation")
