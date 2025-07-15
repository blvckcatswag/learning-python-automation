def sum_numbers_from_string(s: str) -> str:
    try:
        numbers = [float(item) for item in s.split(',')]
        total = int(sum(numbers))
        return str(total)
    except ValueError:
        return "Не можу це зробити"

# Тестовый список
data = ["1,2,3,4", "12,3,4.50", "qwerty,1,2,3"]

for item in data:
    print(sum_numbers_from_string(item))
