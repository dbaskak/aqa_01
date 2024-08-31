adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("Task 1:")
correct_adwentures = adwentures_of_tom_sawer.replace("\n", " ")
print(correct_adwentures)

# task 02 ==
""" Замініть .... на пробіл
"""
print("Task 2:")
correct_adwentures = correct_adwentures.replace("....", " ")
print(correct_adwentures)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print("Task 3:")
correct_adwentures = " ".join(correct_adwentures.split())
print(correct_adwentures)
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("Task 4:")
number_of_h = adwentures_of_tom_sawer.count("h")
print(number_of_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("Task 5:")
words = adwentures_of_tom_sawer.split()
upper_case_letters = sum(1 for word in words if word[0].isupper())
print(f"Amount of capital letters is: {upper_case_letters}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("Task 6:")
first_position = adwentures_of_tom_sawer.find("Tom")
second_position = adwentures_of_tom_sawer.find("Tom", first_position + 1)
print(second_position)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("Task 7:")
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.replace("\n", " ").replace("....", " ")
adwentures_of_tom_sawer_sentences = " ".join(adwentures_of_tom_sawer_sentences.split())
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("Task 8:")
sentence = adwentures_of_tom_sawer_sentences.split('. ')
print(sentence[-1])

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("Task 9:")
start_with = "By the time"
position = adwentures_of_tom_sawer.find(start_with)
if position:
    print(True)
else:
    print(False)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("Task 10:")
last_sentence = sentence[-1]
count = len(last_sentence.split())
print(f"There are {count} words in the last sentence")

