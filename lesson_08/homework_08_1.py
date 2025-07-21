def sum_numbers_from_string(s: str) -> str:
    """
    Преобразует строку с числами, разделёнными запятой, в сумму этих чисел.
    Если строка содержит некорректные данные — возвращает сообщение об ошибке.
    """
    try:
        numbers = [float(item) for item in s.split(',')]
        total = int(sum(numbers))
        return str(total)
    except ValueError:
        return "Не можу це зробити"


data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in data:
    print(sum_numbers_from_string(item))
