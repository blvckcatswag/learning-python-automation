"""
Task 3 from homework 7
"""
def arithmetic_mean(numbers):
    '''Вычисляет среднее арифметическое значение списка чисел'''
    return sum(numbers) / len(numbers)


"""
Task 4 from homework 7
"""
def revers_str(string):
    '''Возвращает перевернутую строку'''
    if not isinstance(string, str):
        raise TypeError("Expected a string") #Добавил для негативного кейса в test_homework_09
    return string[::-1]


"""
Task 7 from homework 7
"""
def even_nums_sum(numbers):
    '''Считает сумму всех чётных чисел в списке'''
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("Все элементы должны быть целыми числами") #Добавил для негативного кейса в test_homework_09
    return sum(x for x in numbers if x % 2 == 0)




if __name__ == "__main__":
    print(arithmetic_mean([1, 2, 3, 4, 5]))
    print(revers_str(None))
    print(even_nums_sum([2, 4, 6, 8, 10]))

