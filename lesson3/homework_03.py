# task 01
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n' \
'"That depends a good deal on where you want to get to," said the Cat.\n' \
'"I don\'t much care where ——" said Alice.\n' \
'"Then it doesn\'t matter which way you go," said the Cat.\n' \
'"—— so long as I get somewhere," Alice added as an explanation.\n' \
''"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
"кавычки уже экранированы с помощью \ внутри строки"
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
seas_together = black_sea + azov_sea
print(f"Площадь чёрного и азовского морей вместе, составляет {seas_together} квадратных километров")
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
products_all = 375291
warehouse1_and_warehouse2 = 250449
warehouse2_and_warehouse3 = 222950
warehouse2 = (warehouse1_and_warehouse2 + warehouse2_and_warehouse3) - products_all
warehouse1 = 250449 - warehouse2
warehouse3 = 222950 - warehouse2
print(f"На первом складе {warehouse1} товар \nНа втором складе {warehouse2} товаров \nНа третьем складе {warehouse3} товара")
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
term = round(12 * 1.5)
monthly_payment = 1179
computer_price = term * monthly_payment
print(f"Цена компьютера составляет {computer_price} гривны")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f"""Остаток от деления 8019 на 8 равен {a}
Остаток от деления 9907 на 9 равен {b}
Остаток от деления 2789 на 5 равен {c}
Остаток от деления 7248 на 6 равен {d}
Остаток от деления 7128 на 5 равен {e}
Остаток от деления 19224 на 9 равен {f}""" )
                                        


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_quantity = 4
big_pizza_price = 274
money_for_big_pizza = big_pizza_quantity * big_pizza_price

medium_pizza_quantity = 2
medium_pizza_price = 218
money_for_medium_pizza = medium_pizza_quantity * medium_pizza_price

juice_quantity = 4
juice_price = 35
money_for_juice = juice_quantity * juice_price

cake_quantity = 1
cake_price = 350
money_for_cake = cake_quantity * cake_price

water_quantity = 3
water_price = 21
money_for_water = water_quantity * water_price

money_needed = ( money_for_big_pizza + money_for_medium_pizza + money_for_juice + money_for_cake + money_for_water )
print(f"Чтобы сделать заказ Иринке необходимо {money_needed} гривен")



# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_total = 232
photo_per_page = 8
page_needed = 232 % 8
if page_needed ==  0:
  print(f"Игорю необходимо {photo_total //  photo_per_page} страниц")
else:
  print(f"Игорю необходимо {photo_total //  photo_per_page} полных страницы и {page_needed} фотографий останется на \nпоследнюю страницу")
#Производить вычисления в print не комильфо, но функции def и остальное мы ещё не проходили. Да и в целом
#можно было решить куда проще, захотел проверить свои силы в if elif else

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
gasoline_consumption = 9
tank_capacity = 48
gasoline_for_whole_distance = round((distance / 100) * gasoline_consumption)
refuelling_needed = round(gasoline_for_whole_distance / tank_capacity)
print(f"1) Для поездки семье понадобится {gasoline_for_whole_distance} литров бензина"
f"\n2)Минимум {refuelling_needed} раз необходимо будет заехать сeмье на заправку за время поездки")
#Тут я не использовал int или целочисленное деление так как при этих способах 1.9 станет 1 а для бензина и расстояния
# это критично