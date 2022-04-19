import random

answer = random(1,10)

while true:
    print("What number?", end ="")
    number = int(input())

    if answer == number:
        print("OK")
        break
    elif answer > number:
        print("Bigger")
    else
        print("Smaller")

