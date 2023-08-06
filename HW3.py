#Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові. Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'". Слово та номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".
while True:
    user_input = input('Введіть слово: ')
    if len(user_input) > 1:
        symbol = user_input[1]
        print(f'The 2 symbol in \'{user_input}\' is \'{symbol}\'')
        break
    elif len(user_input) == 1:
        symbol = user_input[0]
        print(f'The 1 symbol in \'{user_input}\' is \'{symbol}\'')
        break
    else:
        len(user_input) < 1
        print('Wrong ENTER anything')

#
