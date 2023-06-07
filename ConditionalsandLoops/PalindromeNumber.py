#Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.

num = int(input())
temp = num
rev = 0

while(num > 0):
    rev = rev * 10 + num%10
    num = num // 10

if(temp == rev):
    print("true")
else:
    print("false")
