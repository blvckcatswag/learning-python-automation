#Порахувати кількість унікальних символів в строці.
#Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()


def symbols_calculate(symbol_string):
    if symbol_string == "":
        return "Строка не должна быть пустой"

    filtered_string = symbol_string.replace(" ", "")

    unique_symbols = set(filtered_string)
    unique_symbols_count = len(unique_symbols)

    return unique_symbols_count >= 10

user_input = input("Введите строку: ")
result = symbols_calculate(user_input)
print(result)