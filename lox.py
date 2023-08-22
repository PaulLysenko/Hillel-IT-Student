user_arg1 = input('Введіть перший аргумент: ')
user_arg2 = input('Введіть другий аргумент: ')

def process_arguments(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1 * arg2
    elif isinstance(arg1, str) and isinstance(arg2, str):
        return arg1 + arg2
    else:
        return (arg1, arg2)

result = process_arguments(user_arg1, user_arg2)
print(f'result is {result}')