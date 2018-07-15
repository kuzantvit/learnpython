#number = 42
import random
number = random.randint(0, 1000)
while True:
    answer = input('Введите число: ')
    if not answer.isdigit():
        print('Vvedite chislo')
        continue
    answer = int(answer)
    if answer > number:
        print('Заданное число больше требуемого')
    elif answer < number:
        print("Заданное число меньше требуемого")
    else:
        break
print("\n\nYou are RIGHT!!!" + '\n' + 'The number is: '+str(number))