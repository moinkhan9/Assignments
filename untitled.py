#Q1. Sort list of tuples using Lambda

data = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]

# Sorting based on the integer value (index 1 of the tuple)
sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)


#Q2. Squares of numbers using Lambda and Map

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map to apply the square lambda function to each element
squares = list(map(lambda x: x**2, numbers))

print(squares)


#Q3. Convert list of integers to tuple of strings

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mapping each integer to a string and converting the result to a tuple
string_tuple = tuple(map(lambda x: str(x), given_list))

print(string_tuple)


#Q4. Product of numbers 1 to 25 using Reduce
from functools import reduce

# Creating a list from 1 to 25
nums_1_to_25 = list(range(1, 26))

# Using reduce to multiply all numbers in the list
product = reduce(lambda x, y: x * y, nums_1_to_25)

print(product)


#Q5. Filter numbers divisible by 2 and 3
num_list = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

# Filtering numbers that satisfy both conditions (divisible by 2 AND 3)
filtered_nums = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, num_list))

print(filtered_nums)


#Q6. Find palindromes using Lambda and Filter

strings = ['python', 'php', 'aba', 'radar', 'level']

# A palindrome is a string that reads the same backwards (s == s[::-1])
palindromes = list(filter(lambda s: s == s[::-1], strings))

print(palindromes)

