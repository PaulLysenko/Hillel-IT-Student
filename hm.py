def is_valid_age(age):
    try:
        age = int(age)
        if age <= 0:
            print('Щось не дуже схоже на вік!')
            return False
        return True
    except ValueError:
        print('Некоректний формат віку. Введіть число.')
        return False

def check_age_and_show_message(age):
    if '7' in str(age):
        print('Вам пощастить!')
    elif age < 16:
        print('Це фільм для дорослих!')
    elif age > 65:
        print('Покажіть пенсійне посвідчення!')
    elif age < 6:
        print('Де твої батьки?')
    else:
        print('А білетів вже немає!')

while True:
    age_input = input('Введіть ваш вік: ')
    if is_valid_age(age_input):
        age = int(age_input)
        check_age_and_show_message(age)
        break