#Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. Якщо перетворити не вдається функція має повернути 0.
user_input = input('Введіть аргумент: ')

def convertor(input_value):
    try:
        res = float(input_value)

    except ValueError:
        res = 0

    return res

result = convertor(user_input)
print(f'result is {result}')

# Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів
# якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# у будь-якому іншому випадку повернути кортеж з цих аргументів

def double_agr_function(arg1, arg2):
    if type(arg1) in (int, float) and type(arg2) in (int, float):
        res = arg1 * arg2
    elif type(arg1) is (str) and type(arg2) is (str):
        res = arg1 + arg2
    else:
        res = tuple((arg1, arg2))

    return res

result1 = double_agr_function(5, 3)
print(f'Result 1: {result1}')

result2 = double_agr_function('Hello, ', 'world!')
print(f'Result 2: {result2}')

result3 = double_agr_function(7, 'string')
print(f'Result 3: {result3}')

#Касир в кінотеатрі 2.0:

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

def cinema_cashier():
    while True:
        age_input = input('Введіть ваш вік: ')
        if is_valid_age(age_input):
            age = int(age_input)
            check_age_and_show_message(age)
            return
cinema_cashier()
