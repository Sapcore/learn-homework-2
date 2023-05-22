import string

"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as f:
        full_text = f.read()
        print(
            f'Количество символов в тексте: {len(full_text)}.')
        text_modified = full_text
        for char in string.punctuation:
            text_modified = text_modified.replace(char, '')
        print(
            f'Количество слов в тексте: {len(text_modified.split())}.')
        full_text = full_text.replace('.', '!')

    with open('referat2.txt', 'w', encoding='utf-8') as f:
        f.write(full_text)


if __name__ == "__main__":
    main()
