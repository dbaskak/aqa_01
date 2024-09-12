# function to calculate the sum of an array

def calculate_sum_strings(s):
    try:
        # devide strings devided by commas into elements
        numbers = [int(num) for num in s.split(',')]
        return sum(numbers)
    except ValueError:
        #if not a number in a string
        return "Can't do the operation"

# a given array:
array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# iterating through the array:
results = [calculate_sum_strings(item) for item in array]

# print results
for result in results:
    print(result)