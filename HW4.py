#Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні літери підряд.
def count_words_with_double_vowels(text):
    vowels = "аеиіїоуюя"
    word_list = text.split()
    count = 0

    for word in word_list:
        consecutive_vowels = 0
        for letter in word:
            if letter.lower() in vowels:
                consecutive_vowels += 1
                if consecutive_vowels == 2:
                    count += 1
                    break
            else:
                consecutive_vowels = 0

    return count

while True:
    input_text = input("Введіть текст: ")
    if input_text.isalpha():
        word_count = count_words_with_double_vowels(input_text)
        print(f"Кількість слів з двома голосними літерами підряд: {word_count}")
        break
    else:
        print('Введіть текс із літер!')

#Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.
lower_limit = 35.9
upper_limit = 37.339
stores = {"cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324,"x-store": 37.166, "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}

for dict_value in stores.items():
    if lower_limit < dict_value[1] < upper_limit:
        print(f'price match: "{dict_value[0]}", {dict_value[1]}')
