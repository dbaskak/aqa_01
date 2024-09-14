# task 6
def find_substring(str1, str2):
    return str1.find(str2)

# task 7 (homework_06_1)
# function calculates if there are more than 10 unique chars in the string and returns True or False
def string_unique_chars_more_than_ten(string):
    unique_chars = len(set(string))
    return unique_chars > 10

# task 8 (homework_06_2)
# function checks input for "h" letter in the word and prints a result
def letter_h_check(word):
        if 'h' in word.lower():
            return "Thanks!"
        else:
            return "Please try again!"

# task 9 (homework_06_3)
# function makes and prints a new list containing strings only
def list_of_string(list1):
    return [item for item in list1 if isinstance(item, str)]

# task 10 (homework_06_4)
# function prints the sum of even of given numbers list
def even_sum(numbers):
    return sum(num for num in numbers if num % 2 == 0)
