
text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

words = text.split()  # разбиваем текст на слова с сохранением знаков препинания

new_words = []

for word in words:  # проходим по каждому слову
    if word[-1] in ',.':  # проверяем, если слово заканчивается на запятую или точку
        new_word = word[:-1] + 'ing' + word[-1]  # добавляем 'ing' перед знаком препинания
    else:
        new_word = word + 'ing'
    new_words.append(new_word)

new_text = ' '.join(new_words)  # объединяем слова обратно в строку

print(new_text)
