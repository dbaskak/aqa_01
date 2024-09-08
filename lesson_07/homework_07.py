# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            print("The result is greater than 25")
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(6)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def summ_of_two(a, b):
    return a + b


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average(list_of_numbers):
    if len(list_of_numbers) == 0:
        return 0
    return sum(list_of_numbers) / len(list_of_numbers)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_string(string):
    return string[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(words):
    if len(words) == 0:
        return None
    return max(words, key=len)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1


# task 7 (homework_06_1)
# function calculates if there are more than 10 unique chars in the string and returns True or False
def string_unique_chars_more_than_ten(string):
    unique_chars = len(set(string))
    if unique_chars > 10:
        return True
    else:
        return False


string_unique_chars_more_than_ten("some string...")


# task 8 (homework_06_2)
# function checks input for "h" letter in the word and prints a result
def letter_h_check(letter):
    while True:
        word = input("Enter any word containing letter 'h' (both lower and upper case): ")
        if 'h' in word.lower():
            print("Thanks!")
            break
        else:
            print("Please try again!")


letter_h_check("word")


# task 9 (homework_06_3)
# function makes and prints a new list containing strings only
def list_of_string(list1):
    list2 = [item for item in list1 if isinstance(item, str)]
    print(list2)


list_of_string(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])


# task 10 (homework_06_4)
# function prints the sum of even of given numbers list
def even_sum(numbers):
    sum_even = sum(num for num in numbers if num % 2 == 0)
    print(f"The sum of all even is equal {sum_even}")


even_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
