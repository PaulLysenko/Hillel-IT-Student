#Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові. Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'". Слово та номер символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".
while True:
    user_input1 = input('Введіть слово: ')
    if user_input1.isalpha():
        if len(user_input1) > 1:
            symbol = user_input1[1]
            print(f'The 2 symbol in \'{user_input1}\' is \'{symbol}\'')
            break
        elif len(user_input1) == 1:
            symbol = user_input1[0]
            print(f'The 1 symbol in \'{user_input1}\' is \'{symbol}\'')
            break
        else:
            if len(user_input1) < 1:
                print('Помилка, ВВЕДІТЬ слово!')
    else:
        print(f'Щось "{user_input1}" не дуже схоже на слово!')

#Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код, який визначить кількість слів, в цих даних.
while True:
    user_input2 = input('Введіть речення: ')
    if user_input2.isalpha():
        if len(user_input2) == 1:
            print(f'Кількість слів у реченні \'{user_input2}\' дорівнює 1.')
            break
        elif len(user_input2) > 1:
            correct = user_input2.strip(' ')
            count = correct.count(' ') + 1
            print(f'Кількість слів у реченні \'{user_input2}\' дорівнює {count}.')
            break
        else:
            if len(user_input2) < 1:
                print('Помилка введіть РЕЧЕННЯ!')
    else:
        print(f'Щось "{user_input2}" не дуже схоже на речення!')

#Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
list1 = [1.4, '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0.6, 'Lorem Ipsum']
list2 = []
for list_elements in list1:
    if type(list_elements) in (int, float):
        list2.append(list_elements)
print(list2)