text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = text.split()

new_words = []
for word in words:
    if word[-1] in ',.':
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        new_word = word + 'ing'
    new_words.append(new_word)
new_text = ' '.join(new_words)  # объединяем слова обратно в строку
print(new_text)

# Исходный текст
text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

# Разделяем текст на слова
words = text.split()

# Список для хранения новых слов
new_words = []

# Обработка каждого слова
for word in words:
    # Проверяем, заканчивается ли слово на запятую или точку
    if word[-1] in ',.':
        # Если заканчивается, добавляем 'ing' перед знаком препинания
        new_word = word[:-1] + 'ing' + word[-1]
    else:
        # Если не заканчивается, просто добавляем 'ing'
        new_word = word + 'ing'
    # Добавляем новое слово в список
    new_words.append(new_word)

# Объединяем новые слова обратно в строку
new_text = ' '.join(new_words)

# Выводим результат
print(new_text)
