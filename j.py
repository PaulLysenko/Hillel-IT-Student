def get_age_form(age):
    age_forms = {
        1: "рік",
        2: "роки",
        3: "роки",
        4: "роки",
        5: "років",
        6: "років",
        7: "років",
        8: "років",
        9: "років",
        0: "років"
    }
    last_digit = age % 10
    if age % 100 in range(10, 20):
        return "років"
    else:
        return age_forms[last_digit]

while True:
    age_input = input('Введіть ваш вік: ')
    if age_input.isdigit():
        age = int(age_input)
        age_form = get_age_form(age)

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
    else:
        print('Щось не дуже схоже на вік!')