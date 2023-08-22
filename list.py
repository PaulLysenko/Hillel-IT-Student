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
            return False, 'Щось не дуже схоже на вік!'
        return True, age
    except ValueError:
        return False, 'Некоректний формат віку. Введіть ЧИСЛО!'

def check_age_and_show_message(age):
    if '7' in str(age):
        message = f'Вам {age} {get_age_form(age)}, вам пощастить!'
    elif age < 16:
        message = f'Тобі лише {age} {get_age_form(age)}, а це фільм для дорослих!'
    elif age > 65:
        message = f'Вам {age} {get_age_form(age)}? Покажіть пенсійне посвідчення!'
    elif age < 7:
        message = f'Тобі ж {age} {get_age_form(age)}! Де твої батьки?'
    else:
        message = f'Незважаючи на те, що вам {age} {get_age_form(age)}, білетів всеодно нема!'
    return message

def cinema_cashier():
    while True:
        age_input = input('Введіть ваш вік: ')
        is_valid, age = is_valid_age(age_input)
        if is_valid:
            message = check_age_and_show_message(age)
            print(message)
            return

cinema_cashier()
