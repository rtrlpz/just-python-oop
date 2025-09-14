import random

lottery_number = []

for i in range(0, 6):
    number = random.randint(1, 50)
    while number in lottery_number:
        number = random.randint(1, 50)

    lottery_number.append(number)

lottery_number.sort()

print(lottery_number)

