# Створіть файл lib.py, помістіть в нього функції вашої програми "Касир". Імпортуйте функції для основної функції гри в основний файл. Запустіть "Касир" з основного файлу
import lib
@lib.decorator
def cinema_cashier():
    while True:
        age_input = input('Введіть ваш вік: ')
        if lib.is_valid_age(age_input):
            age = int(age_input)
            age_form = lib.get_age_form(age)
            lib.check_age_and_show_message(age, age_form)
            return