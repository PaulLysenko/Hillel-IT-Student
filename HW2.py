#Касир в кінотеатрі:

while True:
    user_input = input('Введіть Ваш вік : ')
    if user_input.isdigit():
        user_input = int(user_input)
        if '7' in str(user_input):
            print('Вам пощастить!')
        elif user_input < 6:
            print('Де твої батьки?')
        elif user_input < 16:
            print('Це фільм для дорослих!')
        elif user_input > 65:
            print('Покажіть пенсійне посвідчення!')
        else:
            print('А білетів вже немає!')
        break
    else:
        print('Помилка! Введіть ЧИСЛО.')