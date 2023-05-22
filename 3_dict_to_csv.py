import csv

"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    friends = [
        {'name': 'Alex', 'age': 28, 'job': 'Engineer'},
        {'name': 'Jane', 'age': 30, 'job': 'Doctor'},
        {'name': 'Johnnie', 'age': 26, 'job': 'Student'},
        {'name': 'Bob', 'age': 47, 'job': 'Janitor'},
        {'name': 'Mickey', 'age': 20, 'job': 'Rock-star'},
        {'name': 'Gregg', 'age': 45, 'job': 'Driver'}
    ]

    with open('people.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=',')
        writer.writeheader()
        for friend in friends:
            writer.writerow(friend)


if __name__ == "__main__":
    main()
