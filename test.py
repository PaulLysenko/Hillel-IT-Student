def count_words_with_double_vowels(text):
    vowels = "аеиіоуюя"
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


input_text = input("Введіть текст: ")
word_count = count_words_with_double_vowels(input_text)
print(f"Кількість слів з двома голосними літерами підряд: {word_count}")


def count_words_with_double_vowels(text):
    vowels = "аеиіїоуюяАЕИІЇОУЮЯ"
    word_list = text.split()
    count = 0

    for word in word_list:
        consecutive_vowels = 0
        for letter in word:
            if letter in vowels:
                consecutive_vowels += 1
                if consecutive_vowels == 2:
                    count += 1
                    break
            else:
                consecutive_vowels = 0

    return count


input_text = input("Введіть текст: ")
word_count = count_words_with_double_vowels(input_text)
print(f"Кількість слів з двома голосними літерами підряд: {word_count}")
