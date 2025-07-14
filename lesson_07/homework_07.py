# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number * multiplier <= 25.:
        result = number * multiplier
        # десь тут помила, а може не одна
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def summation(num1, num2):
    '''Складывает два числа'''
    return num1 + num2


print(summation(3, 4))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def arithmetic_mean(numbers):
    '''Вычисляет среднее арифметическое значение списка чисел'''
    return sum(numbers) / len(numbers)


print(arithmetic_mean([1, 2, 3, 4, 5]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def revers_str(string):
    '''Возвращает перевернутую строку'''
    return string[::-1]


print(revers_str("Hello, world!"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_substring(list1):
    '''Возвращает самое длинное слово в строке'''
    return max(list1, key=len)


print(longest_substring(['a', 'qq', 'www', 'cccc', 'My name is Python', 'London is the capital of great britain']))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    '''Проверят  является ли строка2 подстрокой строки1'''
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
"""
Домашка 6.4
Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
"""


def even_muns_sum(numbers):
    '''Считает сумму всех чётных чисел в списке'''
    return sum(x for x in numbers if x % 2 == 0)


print(even_muns_sum([72, 65, 24, 89, 57, 30, 41, 98, 86, 44, 92, 29, 1, 12,
                     60, 6, 23, 91, 55, 4, 36, 17, 19, 90, 100,
                     13, 78, 34, 8, 66, 27, 49, 31, 10, 2, 15, 21, 64, 81, 26]))
# task 8
"""
Домашка 6.3
Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
#Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
#Данні в лісті можуть бути будь якими
"""
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []


def strint_return(list1):
    '''Возвращает список, который содержит только строки'''
    return [x for x in lst1 if isinstance(x, str)]


print(strint_return(lst1))

# task 9
"""
Задача 9 из домашки 1:
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""


def count_children_today():
    all_boys = 24
    all_girls = all_boys // 2

    boys_today = all_boys - 1
    girls_today = all_girls - 2

    childrens_today = boys_today + girls_today
    print("Детей всего сегодня:", childrens_today)


count_children_today()

# task 10
"""
Задача 10 из домашки 1:
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""


def total_books_price():
    first_book_price = 8
    second_book_price = first_book_price + 2
    third_book_price = (first_book_price + second_book_price) / 2

    all_books_price = first_book_price + second_book_price + third_book_price
    print("Цена за все книги составила:", all_books_price)


total_books_price()

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
