import unittest

from aqa_01.lesson_09.src.homeworks import find_substring, string_unique_chars_more_than_ten, letter_h_check, \
    list_of_string, even_sum


# test suit TestFindSubstring for task_6
class TestFindSubstring(unittest.TestCase):
    # test case 1
    def test_substring_found(self):
        self.assertEqual(find_substring("Hello, World!", "World"), 7)
        self.assertEqual(find_substring("Python programming", "Python"), 0)

    # test case 2
    def test_substring_not_found(self):
        self.assertEqual(find_substring("The quick brown fox", "cat"), -1)
        self.assertEqual(find_substring("Data science", "math"), -1)

    # test case 3
    def test_empty_substring(self):
        self.assertEqual(find_substring("Some string", ""), 0)
        self.assertEqual(find_substring("", "Some string"), -1)

    # test case 4
    def test_both_substrings_empty(self):
        self.assertEqual(find_substring("", ""), 0)

# test suit TestStringUniqueChars for task_7
class TestStringUniqueChars(unittest.TestCase):

# test case 1
    def test_more_than_ten_unique_chars(self):
        self.assertTrue(string_unique_chars_more_than_ten("abcdefghijk")) # 11 unique chars
        self.assertTrue(string_unique_chars_more_than_ten("12345abcdefg")) # 12 unique chars

# test case 2
    def test_ten_or_less_unique_chars(self):
        self.assertTrue(string_unique_chars_more_than_ten("abcdefghij")) # == 10 unique chars
        self.assertTrue(string_unique_chars_more_than_ten("abcde"))  # 5 unique chars

# test case 3
    def test_empty_string(self):
        self.assertFalse(string_unique_chars_more_than_ten("")) # empty string

# test suit TestLetterHCheck for task_8
class TestLetterHCheck(unittest.TestCase):
# test case 1
    def test_contains_lowercase_h(self):
        self.assertEqual(letter_h_check("hello"), "Thanks!") # string contains letter h lowercase

# test case 2
    def test_contains_uppercase_h(self):
        self.assertEqual(letter_h_check("Hello"), "Thanks!") # string contains letter h uppercase

# test case 3
    def test_no_h(self):
        self.assertEqual(letter_h_check("world"), "Please try again!") # no letter h

# test case 4
    def test_empty_string(self):
        self.assertEqual(letter_h_check(""), "Please try again!") # empty string

# test suit TestListOfString for task_9
class TestListOfString(unittest.TestCase):
    # test case 1
    def test_only_strings(self):
        self.assertEqual(list_of_string(["apple", "banana", "cherry"]), ["apple", "banana", "cherry"])
    # test case 2
    def test_strings_and_other_types(self):
        self.assertEqual(list_of_string(["apple", 123, "banana", [1, 2], "cherry"]), ["apple", "banana", "cherry"])

    # test case 3
    def test_empty_list(self):
        self.assertEqual(list_of_string([]), [])

    # test case 4
    def test_no_strings(self):
        self.assertEqual(list_of_string([123, 456, [1, 2], {"key": "value"}]), [])

# test suit TestEvenSum for task_10
class TestEvenSum(unittest.TestCase):

    # test case 1
    def test_all_even(self):
        self.assertEqual(even_sum([2, 4, 6, 8]), 20)

    # test case 2
    def test_mix_of_even_and_odd(self):
        self.assertEqual(even_sum([1, 2, 3, 4, 5]), 6)

    # test case 3
    def test_no_even(self):
        self.assertEqual(even_sum([1, 3, 5, 7]), 0)

    # test case 4
    def test_empty_list(self):
        self.assertEqual(even_sum([]), 0)

    # test case 5
    def test_negative_even_numbers(self):
        self.assertEqual(even_sum([-2, -4, -6, 3, 5]), -12)

if __name__ == '__main__':
    unittest.main
