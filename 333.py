def get_age_form(age):
    if age % 10 == 1 and age % 100 != 11:
        return "рік"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "роки"
    else:
        return "років"

def is_valid_age(age):
    try:
        age = int(age)
        if age <= 0:
            print('Щось не дуже схоже на вік!')
            return False
        return True
    except ValueError:
        print('Некоректний формат віку. Введіть ЧИСЛО!')
        return False

def check_age_and_show_message(age):
    age_form = get_age_form(age)  # Вызываем get_age_form() здесь и сохраняем результат в переменной age_form
    if '7' in str(age):
        print(f'Вам {age} {age_form}, вам пощастить!')
    elif age < 16:
        print(f'Тобі лише {age} {age_form}, а це фільм для дорослих!')
    elif age > 65:
        print(f'Вам {age} {age_form}? Покажіть пенсійне посвідчення!')
    elif age < 7:
        print(f'Тобі ж {age} {age_form}! Де твої батьки?')
    else:
        print(f'Незважаючи на те, що вам {age} {age_form}, білетів всеодно нема!')

def cinema_cashier():
    while True:
        age_input = input('Введіть ваш вік: ')
        if is_valid_age(age_input):
            age = int(age_input)
            check_age_and_show_message(age)
            return
cinema_cashier()