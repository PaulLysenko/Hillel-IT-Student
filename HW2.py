#Касир в кінотеатрі:
import sys


user_input = input('Введіть Ваш вік : ')
if user_input.__contains__('7'):
    print('Вам пощастить!')
    sys.exit()
while True:
    if user_input.isdigit():
        user_input = int(user_input)
        break
    else:
        print('Помилка! Введіть ЧИСЛО.')
if user_input < 6:
    print('Де твої батьки?')
elif user_input < 16:
    print('Це фільм для дорослих!')
elif user_input > 65:
    print('Покажіть пенсійне посвідчення!')
else:
    print('А білетів вже немає!')