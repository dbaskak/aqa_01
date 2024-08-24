alice_in_wonderland = """
"'Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don't much care where ——" said Alice.\n
"Then it doesn't matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you're sure to do that," said the Cat, "if you only walk long enough.'"
"""
print(alice_in_wonderland)

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


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
totall_area = black_sea + azov_sea
print(f"The totall area of Black and Azov see is: {totall_area}", end="\n\n" )


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
stores = 375291
first_and_second_stores = 250449
second_and_third_stores = 222950
first_store = stores - second_and_third_stores
third_store = stores - first_and_second_stores
second_store = stores - first_store - third_store
print(f"Items in stores:\n First store: {first_store}\n Second store: {second_store}\n Third store: {third_store}", end="\n\n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
computer_cost = 1179 * 18
print(f"The computer will cost {computer_cost} UAH", end="\n\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("Residue from division 8019 : 8 =",8019 % 8)
print("Residue from division 9907 : 9 =",9907 % 9)
print("Residue from division 2789 : 5 =",2789 % 5)
print("Residue from division 7248 : 6 =",7248 % 6)
print("Residue from division 7128 : 5 =",7128 % 5)
print("Residue from division 19224 : 9 =",19224 % 9, end="\n\n")

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
pizza_big = 274
pizza_mid = 218
juice = 35
cake = 350
water = 21
pizza_big_ammount = 4
pizza_mid_ammount = 2
juice_ammount = 4
cake_ammount = 1
water_ammount = 3
birthday_budget = pizza_big * pizza_big_ammount + pizza_mid * pizza_mid_ammount + juice * juice_ammount + cake * cake_ammount + water * water_ammount

print(f"The birsday-party budget is: {birthday_budget} UAH", end="\n\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
pages_number = 232 // 8
print(f"Igor needs at least {pages_number} photo album", end="\n\n")

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
consumption_100km = 9
consumption_total = (distance * 2) // 100 * 9
tank_litres = 48
print(f"Famaly will fill up full tank at least {consumption_total // tank_litres} times")

