def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру
    root_word = root_word.lower()
    # Создаём пустой список для подходящих слов
    same_words = []

    # Перебираем все остальные слова
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        # Проверяем, содержится ли root_word в слове или слово в root_word
        if root_word in word_lower or word_lower in root_word:
            same_words.append(word)  # Добавляем слово в результат

    return same_words  # Возвращаем список подходящих слов


# Пример вызовов функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результата
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
