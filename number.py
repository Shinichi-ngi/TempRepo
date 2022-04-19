import random

answer = random.randint(1,10)

while True:
    print("What number?", end ="")
    number = int(input())

    if answer == number:
        print("OK")
        break
    elif answer > number:
        print("Bigger")
    else:
        print("Smaller")

