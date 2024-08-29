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
correct_adwentures = adwentures_of_tom_sawer.replace("\n", " ")
print(correct_adwentures)

# task 02 ==
""" Замініть .... на пробіл
"""
correct_adwentures = correct_adwentures.replace("....", " ")
print(correct_adwentures)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
correct_adwentures = " ".join(correct_adwentures.split())
print(correct_adwentures)
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
number_of_h = adwentures_of_tom_sawer.count("h")
print(number_of_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
upper_case_letters = sum(1 for letter in adwentures_of_tom_sawer if letter.isupper())
print(upper_case_letters)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_position = adwentures_of_tom_sawer.find("Tom")
second_position = adwentures_of_tom_sawer.find("Tom", first_position + 1)
print(second_position)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3].lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
start_with = "By the time"
position = adwentures_of_tom_sawer.find(start_with)
print(f"Sentence 'By the time' starts at {position} position")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
count = len(adwentures_of_tom_sawer_sentences[-1].split())
# print(adwentures_of_tom_sawer_sentences[1])
# print(adwentures_of_tom_sawer_sentences[-1])
print(adwentures_of_tom_sawer_sentences[-1].split())

print(f"There are {count} words in the last sentence")

