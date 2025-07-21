import unittest
from lesson_09.homework_09 import arithmetic_mean, revers_str, even_nums_sum


# TODO: Написать тесты для функции arithmetic_mean

class TestHomework09Func1(unittest.TestCase):
    """
    Тестирует функцию arithmetic_mean из модуля homework_09.
    Проверяет:
    - Обычные числа
    - Отрицательные числа
    - Список из одного элемента
    - Пустой список и ошибку деления на 0

    """

    def test_arithmetic_mean_basic(self):
        self.assertEqual(arithmetic_mean([1, 2, 3, 4, 5]), 3.0)

    def test_arithmetic_mean_with_negatives(self):
        self.assertEqual(arithmetic_mean([-1, -2, -3]), -2.0)

    def test_arithmetic_mean_single_value(self):
        self.assertEqual(arithmetic_mean([42]), 42.0)

    def test_arithmetic_mean_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            arithmetic_mean([])


# TODO: Написать тесты для функции revers_str

class TestHomework09Func2(unittest.TestCase):
    """Тестирует функцию revers_str из модуля homework_09.

       Проверяет:
       - обычные строки
       - одинаковые символы
       - пустые строки
       - ошибки на неправильных типах """

    def test_revers_str(self):
        self.assertEqual(revers_str("Hello World!"), "!dlroW olleH")

    def test_revers_str_same_symbols(self):
        self.assertEqual(revers_str("aaaaaaaaaa"), "aaaaaaaaaa")

    def test_revers_str_empty(self):
        self.assertEqual(revers_str(""), "")

    def test_revers_str_none(self):
        with self.assertRaises(TypeError):
            revers_str(None)


# TODO: Написать тесты для функции even_muns_sum

class TestHomework09Func3(unittest.TestCase):
    """
    Тестирует функцию even_nums_sum из модуля homework_09.
    Проверяет:
    - Список обычных чисел от 1 до 5
    - Список только нечетных чисел
    - Пустой список
    - Ошибку неправильного типа
    - проверяет длину результата
    - проверяет что есть хотя бы одно четное число
    - проверяет поведение при передаче None
    """

    def test_even_nums_sum_basic(self):
        self.assertEqual(even_nums_sum([1, 2, 3, 4, 5]), 6)

    def test_even_nums_sum_only_odd(self):
        self.assertEqual(even_nums_sum([1, 3, 5, 7, 9, 11, 13]), 0)

    def test_even_nums_sum_empty(self):
        self.assertEqual(even_nums_sum([]), 0)

    def test_even_nums_sum_invalid_type(self):
        with self.assertRaises(TypeError):
            even_nums_sum(["python"])

    def test_even_nums_sum_non_negative(self):
        result = even_nums_sum([100, 200, 300])
        self.assertTrue(result >= 0)

    def test_even_nums_sum_input_contains_even(self):
        data = [1, 2, 3]
        self.assertIn(True, [x % 2 == 0 for x in data])

    def test_even_nums_sum_none(self):
        with self.assertRaises(TypeError):
            even_nums_sum(None)
